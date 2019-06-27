from Ship import Ship
from Subroutines.States.Condition import Condition


class Health(Condition):
	health_level: int
	minmax: str
	target: str
	
	def __init__(self, health_level: int, minmax: str, target: str):
		self.health_level = health_level
		self.minmax = minmax
		self.target = target
	
	def test(self, own_ship: Ship, enemy_ship: Ship):
		if self.target == "self":
			target_ship = own_ship
		elif self.target == "enemy":
			target_ship = enemy_ship
		else:
			raise Exception('Invalid ship target in Health Conditions')
		
		result = False
		if self.minmax == "max":
			if target_ship.health <= self.health_level:
				result = True
		elif self.minmax == "min":
			if target_ship.health >= self.health_level:
				result = True
		return result
