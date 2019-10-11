from Ship import Ship
from Subroutines.Conditions.Condition import Condition


class Distance(Condition):
	distance: int
	
	def __init__(self, at_least: int, at_most: int, distance: int):
		self.at_least = at_least
		self.at_most = at_most
		self.distance = distance
	
	def test(self, own_ship: Ship, enemy_ship: Ship):
		result = False
		distance = self.calculate_distance(own_ship.location, enemy_ship.location)
		
		if self.at_most is not None:
			if distance <= self.distance:
				result = True
		elif self.at_least is not None:
			if distance >= self.distance:
				result = True
				
		return result
