from Coordinates import Coordinates
from Ship import Ship
from Subroutines.Actions.Action import Action
from Weapon import Weapon


class FireWeapon(Action):
	name = "FireWeapon"
	weapon: Weapon
	
	def __init__(self, weapon: Weapon):
		self.weapon = weapon
	
	def activate(self, ship: Ship, coord: Coordinates):
		self.weapon.fire()
