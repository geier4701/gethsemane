from Models import Computer, ShipType, Radar, JumpDrive, ImpulseEngine, Location


class Ship:
	size: ShipType
	armament: []
	crew: []
	radar: Radar
	jump_drive: JumpDrive
	impulse_engine: ImpulseEngine
	computer: Computer
	location: Location
	impulse_speed: int
	direction: int
	max_energy: int
	current_energy: int
	
	def __init__(self):
		self.location = Location.Location(0, 0, 0)
		self.current_velocity = 0
	
	def jump_move(self, coord):
		if self.current_energy >= self.jump_drive.jump_cost:
			self.location = coord
			self.current_energy -= self.jump_drive.jump_cost
			return True
		else:
			return False
	
	def impulse_move(self, velocity_change):
		# ALTER VELOCITY/DIRECTION
		pass
	
	def update_module_status(self, module, action):
		pass
