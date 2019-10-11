from Models import ShipType, Coordinates
from Components import Computer, ImpulseEngine, Radar, JumpDrive


class Ship:
	ship_class: ShipType
	armament: dict
	crew: dict
	subroutines: list
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
