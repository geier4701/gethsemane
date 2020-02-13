from api.ShipCombat.Models.Ship import Ship
from api.ShipCombat.Models.Subroutines.Conditions.Condition import Condition, Target


class AmmunitionLevel(Condition):
	ammunition_name: str
	
	def __init__(self, at_least: int, at_most: int, ammunition_name: str):
		self.at_least = at_least
		self.at_most = at_most
		self.ammunition_name = ammunition_name
		self.target = Target.SELF
	
	def test(self, own_ship: Ship, enemy_ship: Ship):
		munitions = own_ship.get_components()[self.ammunition_name]
		
		for munition in munitions:
			if self.compare(munition.remaining_ammo):
				return True
		
		return False
