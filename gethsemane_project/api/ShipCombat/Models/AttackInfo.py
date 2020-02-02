from .Components.Ammunition import Ammunition
from .Components.Weapon import Weapon
from .Coordinates import Coordinates


class AttackInfo:
	coord: Coordinates
	weapon: Weapon
	ammo: Ammunition
	
	def __init__(self, coord: Coordinates, weapon: Weapon, ammo: Ammunition):
		self.coord = coord
		self.weapon = weapon
		self.ammo = ammo
