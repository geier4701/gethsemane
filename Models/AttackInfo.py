from Coordinates import Coordinates
from Weapon import Weapon


class AttackInfo:
	coord: Coordinates
	weapon: Weapon
	
	def __init__(self, coord: Coordinates, weapon: Weapon):
		self.coord = coord
		self.weapon = weapon
