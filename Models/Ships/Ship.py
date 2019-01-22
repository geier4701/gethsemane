from Location import Location
from Scanners.Radar import Radar
import ShipType
from Drives import JumpDrive, ImpulseEngine
from Computers import Computer


class Ship:
	s_class: ShipType
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
	
	def __init__(self, s_class, sh_class, armament, crew, r_class, j_class, i_class, c_class):
		self.ship_class = s_class
		self.shield_class = sh_class
		self.armament = armament
		self.crew = crew
		self.radar = r_class
		self.drive_class = j_class
		self.impulse_class = i_class
		self.cpu_class = c_class
		self.location = Location(0, 0, 0)
		self.impulse_speed = 0
	
	def jump_move(self, coord):
		if self.current_energy >= self.jump_drive.jump_cost:
			self.location = coord
			self.current_energy -= self.jump_drive.jump_cost
			return True
		else:
			return False
		pass
	
	def impulse_move(self, velocity_change):
		# ALTER VELOCITY/DIRECTION
		pass
	
	def update_module_status(self, module, action):
		pass
