from api.ShipCombat.Models.Subroutines.Conditions.Condition import Condition, Target


class AmmunitionLevel(Condition):
	ammunition_name: str
	name = 'AL'
	
	def __init__(self, at_least: int, at_most: int, ammunition_name: str):
		self.at_least = at_least
		self.at_most = at_most
		self.ammunition_name = ammunition_name
		self.target = Target.SELF
