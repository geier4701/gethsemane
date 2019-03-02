from Ship import Ship
from Subroutines.States.Condition import Condition
from Weapon import Weapon


class AmmunitionLevel(Condition):
	name = "AmmunitionLevel"
	weapon_id: int
	ammunition_level: int
	minmax: str
	target: str
	
	def __init__(self, weapon_id: int, ammunition_level: int, minmax: str, target: str):
		self.weapon_id = weapon_id
		self.ammunition_level = ammunition_level
		self.minmax = minmax
	
	def test(self, own_ship: Ship, enemy_ship: Ship):
		if self.target == "self":
			target_ship = own_ship
		elif self.target == "enemy":
			target_ship = enemy_ship
		else:
			raise Exception('Invalid ship target in AmmunitionLevel Condition')
		
		to_test = target_ship.armament[self.weapon_id]
		result = False
		if self.minmax == "max":
			if to_test.ammunition <= self.ammunition_level:
				result = True
		elif self.minmax == "min":
			if to_test.ammunition >= self.ammunition_level:
				result = True
		return result
