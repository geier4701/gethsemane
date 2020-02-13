from api.ShipCombat.Models.Components.Component import Component
from api.models import ComputerModel


class Computer(Component):
	speed: int
	capacity: int
	
	def __init__(self, model: ComputerModel):
		self.component_id = model.computer_id
		self.name = model.name
		self.mass = model.mass
		self.repair_cost = model.repair_cost
		self.speed = model.speed
		self.capacity = model.capacity
		self.operational = True
	
	def get_stat_info(self):
		return {
			"id": self.component_id,
			"name": self.name,
			"mass": self.mass,
			"speed": self.speed,
			"capacity": self.capacity
		}
