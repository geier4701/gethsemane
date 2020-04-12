from abc import ABC


class Component(ABC):
	component_id: int
	name: str
	mass: int
	operational: bool
	repair_cost: int
	
	def disable(self):
		self.operational = False
	
	def enable(self):
		self.operational = True
