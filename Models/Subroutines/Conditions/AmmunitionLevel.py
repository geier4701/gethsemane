from Components.Weapon import AmmunitionType
from Ship import Ship
from Subroutines.Conditions.Condition import Condition


class AmmunitionLevel(Condition):
	ammunition_type: AmmunitionType
	
	def __init__(self, at_least: int, at_most: int, ammunition_type: AmmunitionType):
		self.at_least = at_least
		self.at_most = at_most
		self.ammunition_type = ammunition_type
	
	def test(self, own_ship: Ship, enemy_ship: Ship):
		to_test = Condition.get_ammunition(self.ammunition_type, own_ship.ammunitions)
		
		result = False
		for testing in to_test:
			if self.at_most is not None:
				if testing.remaining_ammo <= self.at_most:
					result = True
			elif self.at_least is not None:
				if testing.remaining_ammo >= self.at_least:
					result = True
		
		return result
