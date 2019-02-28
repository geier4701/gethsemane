from Coordinates import Coordinates
from Subroutines.Actions.Action import Action
from Weapon import Weapon


class FireWeapon(Action):
	weapon: Weapon
	
	def __init__(self, weapon: Weapon):
		self.weapon = weapon
	
	def activate(self, coord: Coordinates):
		self.weapon.fire()
