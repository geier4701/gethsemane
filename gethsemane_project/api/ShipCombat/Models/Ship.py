from typing import List

from api.ShipCombat.Models import Coordinates, ShipType
from api.ShipCombat.Models.Components.Ammunition import Ammunition
from api.ShipCombat.Models.Components.Computer import Computer
from api.ShipCombat.Models.Components.ImpulseEngine import ImpulseEngine
from api.ShipCombat.Models.Components.JumpDrive import JumpDrive
from api.ShipCombat.Models.Components.Radar import Radar
from api.ShipCombat.Models.Components.Weapon import Weapon
from api.ShipCombat.Models.Subroutines import Subroutine


class Ship:
	ship_class: str
	armament: List[Weapon]
	ammunitions: List[Ammunition]
	subroutines: List[Subroutine]
	radar: Radar
	jump_drive: JumpDrive
	impulse_engine: ImpulseEngine
	computer: Computer
	location: Coordinates
	battery_max: int
	current_energy: int
	power_gen: int
	health: int
	name: str
	weight: int
	# FUTURE ADDITIONS
	crew: dict
	
	def __init__(self):
		self.location = Coordinates.Coordinates(0, 0, 0)
	
	def get_components(self):
		components = {
			self.radar.name: self.radar,
			self.jump_drive.name: self.jump_drive,
			self.impulse_engine.name: self.impulse_engine,
			self.computer.name: self.computer
		}
		
		for weapon in self.armament:
			components[weapon.name] = weapon
		
		for ammo in self.ammunitions:
			if ammo.name not in components.keys:
				components[ammo.name] = [ammo]
			else:
				components[ammo.name].append(ammo)
		
		return components
	
	def get_subroutines(self):
		pass
