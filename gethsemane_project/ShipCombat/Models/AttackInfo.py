from gethsemane_project.ShipCombat.Models.Components.Ammunition import Ammunition
from gethsemane_project.ShipCombat.Models.Components.Weapon import Weapon
from gethsemane_project.ShipCombat.Models.Coordinates import Coordinates


class AttackInfo:
	coord: Coordinates
	weapon: Weapon
	ammo: Ammunition
	
	def __init__(self, coord: Coordinates, weapon: Weapon, ammo: Ammunition):
		self.coord = coord
		self.weapon = weapon
		self.ammo = ammo
