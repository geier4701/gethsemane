from abc import abstractmethod


class Weapon:
	range: int
	damage_type: str
	operational: bool
	
	def disable(self):
		self.operational = False
	
	def enable(self):
		self.operational = True
	
	@abstractmethod
	def fire(self):
		pass
