from Location import Location
from Radars.Radar import RadarClass
from ShipTypes import ShipType


class Ship:
	s_class: ShipType
	armament: []
	crew: []
	r_class: RadarClass
	d_class: DriveClass
	i_class: ImpulseClass
	c_class: ComputerClass
	location: Location
	impulse_speed: int
	direction: int
	max_energy: int
	current_energy: int
	
	def __init__(self, s_class, sh_class, armament, crew, r_class, d_class, i_class, c_class):
		self.ship_class = s_class
		self.shield_class = sh_class
		self.armament = armament
		self.crew = crew
		self.radar = r_class
		self.drive_class = d_class
		self.impulse_class = i_class
		self.cpu_class = c_class
		self.location = Location(0, 0, 0)
		self.impulse_speed = 0
	
	def jump_move(self, coord):
		# CHECK ENERGY LEVEL
		# MOVE SHIP TO LOCATION
		# DRAIN ENERGY
		pass
	
	def impulse_move(self, velocity_change):
		# ALTER VELOCITY
		pass
	
	def update_module_status(self, module, action):
		pass
