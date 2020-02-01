from abc import ABC, abstractmethod


class Component(ABC):
	component_id: int
	name: str
	mass: int
	operational: bool
	repair_cost: int
	
	@abstractmethod
	def get_stat_info(self):
		pass
	
	def disable(self):
		self.operational = False
	
	def enable(self):
		self.operational = True