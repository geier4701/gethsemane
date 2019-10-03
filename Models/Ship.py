from Models import Computer, ShipType, Radar, JumpDrive, ImpulseEngine, Coordinates, Weapon


class Ship:
	size: ShipType
	armament: {}
	crew: {}
	subroutines: []
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
