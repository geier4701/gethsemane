from Ship import Ship
from Subroutines.Conditions.Condition import Condition


class Distance(Condition):
	
	def __init__(self, at_least: int, at_most: int):
		self.at_least = at_least
		self.at_most = at_most
	
	def test(self, own_ship: Ship, enemy_ship: Ship):
		distance = self.calculate_distance(own_ship.location, enemy_ship.location)
		return self.compare(int(distance))
