from api.ShipCombat.Models.Components.Ammunition import AmmunitionType
from api.ShipCombat.Models.Ship import Ship
from api.ShipCombat.Models.Subroutines.Conditions.Condition import Condition, Target


class AmmunitionLevel(Condition):
	ammunition_type: AmmunitionType
	
	def __init__(self, at_least: int, at_most: int, ammunition_type: AmmunitionType):
		self.at_least = at_least
		self.at_most = at_most
		self.ammunition_type = ammunition_type
		self.target = Target.SELF
	
	def test(self, own_ship: Ship, enemy_ship: Ship):
		munitions = Condition.get_ammunition(self.ammunition_type, own_ship.ammunitions)
		
		for munition in munitions:
			if self.compare(munition.remaining_ammo):
				return True
		
		return False
