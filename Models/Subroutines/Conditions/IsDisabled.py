from Ship import Ship
from Subroutines.Conditions.Condition import Condition, Target


class IsDisabled(Condition):
	component_id: int
	
	def __init__(self, at_least: int, at_most: int, target: Target, component_id: int):
		self.at_least = at_least
		self.at_most = at_most
		self.target = target
		self.component_id = component_id
	
	def test(self, own_ship: Ship, enemy_ship: Ship):
		pass
