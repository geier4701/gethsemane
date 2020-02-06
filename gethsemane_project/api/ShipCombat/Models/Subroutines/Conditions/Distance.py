from api.ShipCombat.Models.Ship import Ship
from api.ShipCombat.Models.Subroutines.Conditions.Condition import Condition, Target


class Distance(Condition):
	
	def __init__(self, at_least: int, at_most: int):
		self.at_least = at_least
		self.at_most = at_most
		self.target = Target.SELF
	
	def test(self, own_ship: Ship, enemy_ship: Ship):
		distance = self.calculate_distance(own_ship.location, enemy_ship.location)
		return self.compare(int(distance))
