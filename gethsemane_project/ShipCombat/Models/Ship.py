from typing import List
from gethsemane_project.ShipCombat.Models import ShipType, Coordinates
from gethsemane_project.ShipCombat.Models.Components.Ammunition import Ammunition
from gethsemane_project.ShipCombat.Models.Components.Computer import Computer
from gethsemane_project.ShipCombat.Models.Components.ImpulseEngine import ImpulseEngine
from gethsemane_project.ShipCombat.Models.Components.JumpDrive import JumpDrive
from gethsemane_project.ShipCombat.Models.Components.Radar import Radar
from gethsemane_project.ShipCombat.Models.Subroutines.Subroutine import Subroutine


class Ship:
	ship_class: ShipType
	armament: dict
	ammunitions: List[Ammunition]
	crew: dict
	subroutines: List[Subroutine]
	radar: Radar
	jump_drive: JumpDrive
	impulse_engine: ImpulseEngine
	computer: Computer
	location: Coordinates
	impulse_speed: int
	direction: int
	max_energy: int
	current_energy: int
	health: int
	
	def __init__(self):
		self.location = Coordinates.Coordinates(0, 0, 0)
	
	def get_components(self):
		components = {
			self.radar.component_id: self.radar,
			self.jump_drive.component_id: self.jump_drive,
			self.impulse_engine.component_id: self.impulse_engine,
			self.computer.component_id: self.computer
		}
		
		for weapon in self.armament:
			components[weapon.component_id] = weapon
		
		return components
