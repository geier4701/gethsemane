from BLL.Horatio import Horatio
from Subroutines.Actions.Action import Action
from Weapon import Weapon


class FireWeapon(Action):
	name = "FireWeapon"
	weapon: Weapon
	
	def __init__(self, weapon: Weapon):
		self.weapon = weapon
	
	def activate(self, captain: Horatio):
		self.weapon.fire(captain.enemy_intel.location)
