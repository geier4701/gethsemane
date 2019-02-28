class Coordinates:
	location: []
	speed: []
	
	def __init__(self, x: int, y: int, z: int):
		self.location = [x, y, z]
		self.speed = [0, 0, 0]
