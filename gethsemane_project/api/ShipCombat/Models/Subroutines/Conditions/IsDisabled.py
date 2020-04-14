from api.ShipCombat.Models.Subroutines.Conditions.Condition import Condition, Target


class IsDisabled(Condition):
	component_name: str
	name = 'IsDisabled'
	
	def __init__(self, condition_id: int, at_least: int, at_most: int, target: Target, component_name: str):
		self.condition_id = condition_id
		self.at_least = at_least
		self.at_most = at_most
		self.target = target
		self.component_name = component_name
