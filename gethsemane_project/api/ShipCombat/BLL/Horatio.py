from typing import List

from api.ShipCombat.Models.Ship import Ship
from api.ShipCombat.Models.Subroutines.Actions.Action import Action
from api.ShipCombat.Models.Subroutines.Conditions.AmmunitionLevel import AmmunitionLevel
from api.ShipCombat.Models.Subroutines.Conditions.Condition import Condition, Target
from api.ShipCombat.Models.Subroutines.Conditions.Distance import Distance
from api.ShipCombat.Models.Subroutines.Conditions.EnergyLevel import EnergyLevel
from api.ShipCombat.Models.Subroutines.Conditions.Health import Health
from api.ShipCombat.Models.Subroutines.Conditions.IsDisabled import IsDisabled


class Horatio:
	own_ship: Ship
	last_action: List[Action]
	enemy_intel: Ship
	
	def __init__(self, ship: Ship):
		self.own_ship = ship
		self.enemy_intel = Ship()
		self.own_ship.current_energy = self.own_ship.battery_max
	
	def command(self):
		# TODO: Move conditions to Horatio class on construction to avoid the circular dependency
		self.own_ship.subroutines.sort(key=lambda sub: subroutine.priority)
		actions_to_take = List[Action]
		for subroutine in self.own_ship.subroutines:
			make_it_so = True
			for condition in subroutine.conditions:
				if not condition.test(self.own_ship, self.enemy_intel):
					make_it_so = False
					break
			
			if make_it_so:
				self.last_action = subroutine.actions
				actions_to_take = subroutine.actions
		
		if not actions_to_take:
			actions_to_take = self.last_action
		
		return actions_to_take
	
	def update_enemy_intel(self, enemy_intel: Ship):
		self.enemy_intel.current_energy = enemy_intel.current_energy
		self.enemy_intel.health = enemy_intel.health
		self.enemy_intel.coordinates = enemy_intel.coordinates
		self.enemy_intel.radar.operational = enemy_intel.radar.operational
		self.enemy_intel.jump_drive.operational = enemy_intel.jump_drive.operational
		self.enemy_intel.impulse_engine.operational = enemy_intel.impulse_engine.operational
		self.enemy_intel.computer.operational = enemy_intel.computer.operational
	
	def reset_ship_weapons(self):
		for weapon in self.own_ship.armament:
			weapon.has_fired = False
	
	def __is_disabled_check(self, condition: Condition) -> bool:
		condition: IsDisabled
		named_components = self.own_ship.get_components()[condition.component_name]
		if hasattr(named_components, "__len__"):
			for component in named_components:
				if component.operational is False:
					return True
			return False
		
		else:
			return named_components.operational
	
	def __ammunition_level_check(self, condition: Condition):
		condition: AmmunitionLevel
		munitions = self.own_ship.get_components()[condition.ammunition_name]
		
		for munition in munitions:
			if condition.compare(munition.remaining_ammo):
				return True
		
		return False
	
	def __distance_check(self, condition: Condition):
		condition: Distance
		distance = condition.calculate_distance(self.own_ship.coordinates, self.enemy_intel.coordinates)
		return condition.compare(int(distance))
	
	def __energy_level_check(self, condition: Condition):
		condition: EnergyLevel
		if condition.target == Target.SELF:
			target_ship = self.own_ship
		elif condition.target == Target.ENEMY:
			target_ship = self.enemy_intel
		else:
			raise Exception('Invalid ship target in EnergyLevel Conditions')
		
		return condition.compare(target_ship.current_energy)
	
	def __health_check(self, condition: Condition):
		condition: Health
		if condition.target == Target.SELF:
			target_ship = self.own_ship
		elif condition.target == Target.ENEMY:
			target_ship = self.enemy_intel
		else:
			raise Exception('Invalid ship target in Health Conditions')
		
		return condition.compare(target_ship.health)
	
	__condition_map = {
		IsDisabled.name: __is_disabled_check,
		AmmunitionLevel: __ammunition_level_check,
		Distance: __distance_check,
		EnergyLevel: __energy_level_check,
		Health: __health_check
	}
	
	def test_condition(self, condition: Condition) -> bool:
		test_condition = self.__condition_map[condition.name]
		return test_condition(self, condition)
