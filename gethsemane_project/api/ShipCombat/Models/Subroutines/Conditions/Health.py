from api.ShipCombat.Models.Subroutines.Conditions.Condition import Condition, Target


class Health(Condition):
	
	def __init__(self, at_least: int, at_most: int, target: Target):
		self.at_least = at_least
		self.at_most = at_most
		self.target = target
	
	def test(self, own_ship, enemy_ship):
		if self.target == Target.SELF:
			target_ship = own_ship
		elif self.target == Target.ENEMY:
			target_ship = enemy_ship
		else:
			raise Exception('Invalid ship target in Health Conditions')
		
		return self.compare(target_ship.health)
