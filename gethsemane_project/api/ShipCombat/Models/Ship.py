from typing import List

from api.ShipCombat.Models.Coordinates import Coordinates
from api.ShipCombat.Models.AttackInfo import AttackInfo
from api.ShipCombat.Models.Components.Ammunition import Ammunition
from api.ShipCombat.Models.Components.Computer import Computer
from api.ShipCombat.Models.Components.ImpulseEngine import ImpulseEngine
from api.ShipCombat.Models.Components.JumpDrive import JumpDrive
from api.ShipCombat.Models.Components.Radar import Radar
from api.ShipCombat.Models.Components.Weapon import Weapon
from api.ShipCombat.Models.Subroutines.Actions.Action import Action
from api.ShipCombat.Models.Subroutines.Actions.AttemptRepairs import AttemptRepairs
from api.ShipCombat.Models.Subroutines.Actions.Delay import Delay
from api.ShipCombat.Models.Subroutines.Actions.FireImpulse import FireImpulse
from api.ShipCombat.Models.Subroutines.Actions.FireWeapon import FireWeapon
from api.ShipCombat.Models.Subroutines.Actions.Jump import Jump
from api.ShipCombat.Models.Subroutines.Actions.Scan import Scan
from api.ShipCombat.Models.Subroutines.Conditions.Condition import Condition
from api.ShipCombat.Models.Subroutines.Subroutine import Subroutine


class Ship:
	ship_class: str
	armament: List[Weapon]
	ammunitions: List[Ammunition]
	subroutines: List[Subroutine]
	radar: Radar
	jump_drive: JumpDrive
	impulse_engine: ImpulseEngine
	computer: Computer
	coordinates: Coordinates
	battery_max: int
	current_energy: int
	power_gen: int
	health: int
	name: str
	weight: int
	# FUTURE ADDITIONS
	crew: dict
	
	def __init__(self):
		self.coordinates = Coordinates(0, 0, 0, 0, 0, 0)
		self.armament = []
		self.ammunitions = []
	
	def get_components(self) -> dict:
		components = {
			self.radar.name: self.radar,
			self.jump_drive.name: self.jump_drive,
			self.impulse_engine.name: self.impulse_engine,
			self.computer.name: self.computer
		}
		
		for weapon in self.armament:
			if weapon.name not in components.keys:
				components[weapon.name] = [weapon]
			else:
				components[weapon.name].append(weapon)
		
		for ammo in self.ammunitions:
			if ammo.name not in components.keys:
				components[ammo.name] = [ammo]
			else:
				components[ammo.name].append(ammo)
		
		return components
	
	def __spend_energy(self, energy_cost) -> bool:
		if self.current_energy >= energy_cost:
			self.current_energy -= energy_cost
			return True
		else:
			return False
	
	def __jump_ship(self, jump: Jump) -> bool:
		if self.__spend_energy(self.jump_drive.energy_cost):
			new_location = Condition.find_desired_coord(jump.distance_from_enemy)
			self.coordinates.speed[0] = self.coordinates.speed[0] + new_location.location[0]
			self.coordinates.speed[1] = self.coordinates.speed[1] + new_location.location[1]
			self.coordinates.speed[2] = self.coordinates.speed[2] + new_location.location[2]
			return True
		else:
			return False
	
	def __fire_impulse_ship(self, fire: FireImpulse) -> bool:
		if self.__spend_energy(self.impulse_engine.energy_cost):
			self.coordinates.speed[0] += fire.velocity_change.speed[0]
			self.coordinates.speed[1] += fire.velocity_change.speed[1]
			self.coordinates.speed[2] += fire.velocity_change.speed[2]
			return True
		else:
			return False
	
	def __delay_ship(self, action: Delay) -> bool:
		return True
	
	def __scan_ship(self, scan: Scan) -> bool:
		return self.__spend_energy(self.radar.energy_cost)
	
	def __attempt_repairs_ship(self, repair: AttemptRepairs) -> bool:
		named_components = self.get_components()[repair.target_component_name]
		target_component = None
		if hasattr(named_components, "__len__"):
			for component in named_components:
				if component.operational is False:
					target_component = component
					
			if target_component is None:
				return False
			
		else:
			target_component = named_components
		
		if self.__spend_energy(target_component.repair_cost):
			target_component.enable()
			return True
		else:
			return False
	
	def __fire_weapon_ship(self, fire_weapon: FireWeapon) -> AttackInfo:
		named_components = self.get_components()[fire_weapon.weapon_name]
		target_weapon = None
		for component in named_components:
			if component.has_fired is False:
				target_weapon = component
		
		ammo_to_check = self.get_components()[target_weapon.ammunition_name]
		
		ammo_to_use = None
		for ammo in ammo_to_check:
			if ammo.remaining_ammo > 0:
				ammo_to_use = ammo
				break
		
		return AttackInfo(target_weapon, ammo_to_use)
	
	__action_map = {
		Jump.name: __jump_ship,
		FireImpulse.name: __fire_impulse_ship,
		Delay.name: __delay_ship,
		Scan.name: __scan_ship,
		AttemptRepairs.name: __attempt_repairs_ship,
		FireWeapon.name: __fire_weapon_ship
	}
	
	def activate(self, action: Action):
		ship_action = self.__action_map[action.name]
		return ship_action(action)
