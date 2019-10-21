from Ship import Ship
from Subroutines.Conditions.Condition import Condition, Target


class AmmunitionLevel(Condition):
	# I DON'T THINK AMMUNITION ID WILL WORK FOR THIS AND FIREWEAPON
	# SEE FIREWEAPON
	ammunition_id: int
	
	def __init__(self, at_least: int, at_most: int, target: Target, ammunition_id: int):
		self.at_least = at_least
		self.at_most = at_most
		self.target = target
		self.ammunition_id = ammunition_id
	
	def test(self, own_ship: Ship, enemy_ship: Ship):
		if self.target == Target.SELF:
			target_ship = own_ship
		elif self.target == Target.ENEMY:
			target_ship = enemy_ship
		else:
			raise Exception('Invalid ship target in AmmunitionLevel Conditions')
		
		to_test = target_ship.armament[self.ammunition_id]
		result = False
		if self.at_most is not None:
			if to_test.ammunition <= self.at_most:
				result = True
		elif self.at_least is not None:
			if to_test.ammunition >= self.at_least:
				result = True
		return result
