from AttackInfo import AttackInfo
from BLL.Horatio import Horatio
from Subroutines.Actions.Action import Action
from Components.Weapon import Weapon


class FireWeapon(Action):
	name = "FireWeapon"
	weapon: Weapon
	attack_info: AttackInfo
	
	def __init__(self, weapon: Weapon):
		self.weapon = weapon
	
	def activate(self, captain: Horatio, info=None):
		# THIS (AND AMMUNITIONLEVEL) NEED A WAY TO CHECK FOR AMMO OF NECESSARY TYPE
		return AttackInfo(info, self.weapon)
