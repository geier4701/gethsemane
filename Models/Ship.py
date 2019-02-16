from Models import Computer, ShipType, Radar, JumpDrive, ImpulseEngine, Location


class Ship:
	size: ShipType
	armament: {}
	crew: {}
	subroutines: []
	radar: Radar
	jump_drive: JumpDrive
	impulse_engine: ImpulseEngine
	computer: Computer
	location: Location
	impulse_speed: int
	direction: int
	max_energy: int
	current_energy: int
	health: int
	
	def __init__(self):
		self.location = Location.Location(0, 0, 0)
	
	def update_module_status(self, module, action):
		pass
