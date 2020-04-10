from typing import List

from api.ShipCombat.BLL.BattleRecorder import BattleRecorder
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
	battle_recorder: BattleRecorder
	
	def __init__(self, ship: Ship, battle_recorder: BattleRecorder):
		self.own_ship = ship
		self.enemy_intel = Ship()
		self.own_ship.current_energy = self.own_ship.ship_class.battery_max
		self.battle_recorder = battle_recorder
	
	def command(self):
		self.own_ship.subroutines.sort(key=lambda sub: sub.priority)
		actions_to_take = []
		for subroutine in self.own_ship.subroutines:
			make_it_so = True
			for condition in subroutine.conditions:
				if not self.test_condition(condition):
					make_it_so = False
					break
			
			if make_it_so:
				self.last_action = subroutine.actions
				actions_to_take = subroutine.actions
				break
		
		if not actions_to_take:
			self.battle_recorder.record_test('NO ACTIONS TO TAKE')
			actions_to_take = self.last_action
		
		return actions_to_take
	
	def update_enemy_intel(self, enemy_intel: Ship):
		# TODO: Add weapons, no weapon status since you cant write a subroutine against a weapon you don't know exists
		self.enemy_intel.current_energy = enemy_intel.current_energy
		self.enemy_intel.ship_class = enemy_intel.ship_class
		self.enemy_intel.coordinates = enemy_intel.coordinates
		self.enemy_intel.radar = enemy_intel.radar
		self.enemy_intel.radar.operational = enemy_intel.radar.operational
		self.enemy_intel.jump_drive = enemy_intel.jump_drive
		self.enemy_intel.jump_drive.operational = enemy_intel.jump_drive.operational
		self.enemy_intel.impulse_engine = enemy_intel.impulse_engine
		self.enemy_intel.impulse_engine.operational = enemy_intel.impulse_engine.operational
		self.enemy_intel.computer = enemy_intel.computer
		self.enemy_intel.computer.operational = enemy_intel.computer.operational
	
	def reset_ship_weapons(self):
		for weapon in self.own_ship.armament:
			weapon.has_fired = False
	
	def __is_disabled_check(self, condition: Condition) -> bool:
		condition: IsDisabled
		named_components = self.own_ship.get_components()[condition.component_name]
		if isinstance(named_components, list):
			for component in named_components:
				if component.operational is False:
					return True
			return False
		
		else:
			return named_components.operational
	
	def __ammunition_level_check(self, condition: Condition):
		condition: AmmunitionLevel
		munitions = self.own_ship.get_components()[condition.ammunition_type]
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
		
		return condition.compare(target_ship.ship_class.health)
	
	__condition_map = {
		IsDisabled.name: __is_disabled_check,
		AmmunitionLevel.name: __ammunition_level_check,
		Distance.name: __distance_check,
		EnergyLevel.name: __energy_level_check,
		Health.name: __health_check
	}
	
	def test_condition(self, condition: Condition) -> bool:
		test_condition = self.__condition_map[condition.name]
		return test_condition(self, condition)
