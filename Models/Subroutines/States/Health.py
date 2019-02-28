from Ship import Ship
from Subroutines.States.Status import Status


class EnergyLevel(Status):
	target: Ship
	health_level: int
	minmax = str
	
	def __init__(self, target: Ship, energy_level: int, minmax: str):
		self.target = target
		self.health_level = energy_level
		self.minmax = minmax
	
	def test(self):
		result = False
		if self.minmax == "max":
			if self.target.health <= self.health_level:
				result = True
		elif self.minmax == "min":
			if self.target.health >= self.health_level:
				result = True
		return result
