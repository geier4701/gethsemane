from api.ShipCombat.Models.Subroutines.Conditions.Condition import Condition, Target


class Health(Condition):
	name = 'Health'
	
	def __init__(self, condition_id: int, at_least: int, at_most: int, target: Target):
		self.condition_id = condition_id
		self.at_least = at_least
		self.at_most = at_most
		self.target = target
