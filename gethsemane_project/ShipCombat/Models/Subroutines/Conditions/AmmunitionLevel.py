from gethsemane_project.ShipCombat.Models.Components.Ammunition import AmmunitionType
from gethsemane_project.ShipCombat.Models.Ship import Ship
from gethsemane_project.ShipCombat.Models.Subroutines.Conditions.Condition import Condition


class AmmunitionLevel(Condition):
	ammunition_type: AmmunitionType
	
	def __init__(self, at_least: int, at_most: int, ammunition_type: AmmunitionType):
		self.at_least = at_least
		self.at_most = at_most
		self.ammunition_type = ammunition_type
	
	def test(self, own_ship: Ship, enemy_ship: Ship):
		munitions = Condition.get_ammunition(self.ammunition_type, own_ship.ammunitions)
		
		for munition in munitions:
			if self.compare(munition):
				return True
		
		return False
