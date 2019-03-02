from Ship import Ship
from Subroutines.States.Condition import Condition


class Distance(Condition):
	range: int
	minmax: str
	
	def __init__(self, minmax: str):
		self.minmax = minmax
	
	def test(self, own_ship: Ship, enemy_ship: Ship):
		result = False
		distance = self.calculate_distance(own_ship.location, enemy_ship.location)
		
		if self.minmax == "max":
			if distance <= self.range:
				result = True
		elif self.minmax == "min":
			if distance >= self.range:
				result = True
				
		return result
