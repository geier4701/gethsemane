class Location:
	coord: []
	speed: []
	
	def __init__(self, x: int, y: int, z: int):
		self.coord = [x, y, z]
		self.speed = [0, 0, 0]
