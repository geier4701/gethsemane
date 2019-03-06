from Models.Component import Component


class Computer(Component):
	speed: int
	capacity: int
	
	def __init__(self, id: int, name: str, mass:int, speed: int, capacity: int):
		self.id = id
		self.name = name
		self.mass = mass
		self.speed = speed
		self.capacity = capacity
	
	def get_stat_info(self):
		return {
			"id": self.id,
			"name": self.name,
			"mass": self.mass,
			"speed": self.speed,
			"capacity": self.capacity
		}
