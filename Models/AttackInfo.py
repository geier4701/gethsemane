from Components import Ammunition
from Coordinates import Coordinates
from Components.Weapon import Weapon


class AttackInfo:
	coord: Coordinates
	weapon: Weapon
	ammo: Ammunition
	
	def __init__(self, coord: Coordinates, weapon: Weapon, ammo: Ammunition):
		self.coord = coord
		self.weapon = weapon
		self.ammo = ammo
