from Ship import Ship
from Subroutines.States.Status import Status
from Weapon import Weapon


class AmmunitionLevel(Status):
	target: Ship
	weapon: Weapon
	ammunition_level: int
	minmax = str
	
	def __init__(self, target: Ship, weapon: Weapon, ammunition_level: int, minmax: str):
		self.target = target
		self.weapon = weapon
		self.ammunition_level = ammunition_level
		self.minmax = minmax
	
	def test(self):
		to_test = self.target.armament[self.weapon.id]
		result = False
		if self.minmax == "max":
			if to_test.ammunition <= self.ammunition_level:
				result = True
		elif self.minmax == "min":
			if to_test.ammunition >= self.ammunition_level:
				result = True
		return result
