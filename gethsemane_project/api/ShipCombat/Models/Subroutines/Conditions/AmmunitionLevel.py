from api.ShipCombat.Models.Components.Ammunition import AmmunitionType
from api.ShipCombat.Models.Subroutines.Conditions.Condition import Condition, Target


class AmmunitionLevel(Condition):
	ammunition_type: AmmunitionType
	name = 'AmmunitionLevel'
	
	def __init__(self, condition_id: int, at_least: int, at_most: int, ammunition_type_name: str):
		self.condition_id = condition_id
		self.at_least = at_least
		self.at_most = at_most
		self.ammunition_type = AmmunitionType(int(ammunition_type_name))
		self.target = Target.SELF
