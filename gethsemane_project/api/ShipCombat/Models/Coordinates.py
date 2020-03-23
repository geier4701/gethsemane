class Coordinates:
	location: list
	speed: list
	
	def __init__(self, l_x: int, l_y: int, l_z: int, s_x: int, s_y: int, s_z: int):
		self.location = [l_x, l_y, l_z]
		self.speed = [s_x, s_y, s_z]
