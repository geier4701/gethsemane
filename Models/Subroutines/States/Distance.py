from Ship import Ship
from Subroutines.States.Condition import Condition


class Distance(Condition):
	distance: int
	minmax: str
	
	def __init__(self, distance: int, minmax: str):
		self.distance = distance
		self.minmax = minmax
	
	def test(self, own_ship: Ship, enemy_ship: Ship):
		result = False
		distance = self.calculate_distance(own_ship.location, enemy_ship.location)
		
		if self.minmax == "max":
			if distance <= self.distance:
				result = True
		elif self.minmax == "min":
			if distance >= self.distance:
				result = True
				
		return result
