from Ship import Ship
from Subroutines.Conditions.Condition import Condition, Target


# THIS IS GOING TO TAKE SOME EXTRA WORK, PARTICULARLY HOW DO YOU CHECK IF AN ENEMY'S
# WEAPON IS DISABLED? YOU DON'T KNOW THEIR COMPONENT ID WHEN BUILDING YOUR SUBROUTINES
class IsDisabled(Condition):
	component_id: int
	
	def __init__(self, at_least: int, at_most: int, target: Target, component_id: int):
		self.at_least = at_least
		self.at_most = at_most
		self.target = target
		self.component_id = component_id
	
	def test(self, own_ship: Ship, enemy_ship: Ship):
		if self.target == Target.SELF:
			target_ship = own_ship
		elif self.target == Target.ENEMY:
			target_ship = enemy_ship
		else:
			raise Exception('Invalid ship target in IsDisabled Conditions')
		
		component = target_ship.get_components()[self.component_id]
		return component.operational
