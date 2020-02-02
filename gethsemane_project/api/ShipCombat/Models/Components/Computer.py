from .Component import Component


class Computer(Component):
	speed: int
	capacity: int
	
	def __init__(self, component_id: int, name: str, mass: int, repair_cost: int, speed: int, capacity: int):
		self.id = component_id
		self.name = name
		self.mass = mass
		self.repair_cost = repair_cost
		self.speed = speed
		self.capacity = capacity
		self.operational = True
	
	def get_stat_info(self):
		return {
			"id": self.id,
			"name": self.name,
			"mass": self.mass,
			"speed": self.speed,
			"capacity": self.capacity
		}
