from Ship import Ship
from Subroutines.Conditions.Condition import Condition, Target


class EnergyLevel(Condition):
	
	def __init__(self, at_least: int, at_most: int, target: Target):
		self.at_least = at_least
		self.at_most = at_most
		self.target = target
	
	def test(self, own_ship: Ship, enemy_ship: Ship):
		if self.target == Target.SELF:
			target_ship = own_ship
		elif self.target == Target.ENEMY:
			target_ship = enemy_ship
		else:
			raise Exception('Invalid ship target in EnergyLevel Conditions')
		
		result = False
		if self.at_most is not None:
			if target_ship.current_energy <= target_ship.current_energy:
				result = True
		elif self.at_least is not None:
			if target_ship.current_energy >= target_ship.current_energy:
				result = True
		return result