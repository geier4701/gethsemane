from AttackInfo import AttackInfo
from BLL.Horatio import Horatio
from Subroutines.Actions.Action import Action
from Weapon import Weapon


class FireWeapon(Action):
	name = "FireWeapon"
	weapon: Weapon
	attack_info: AttackInfo
	
	def __init__(self, weapon: Weapon):
		self.weapon = weapon
	
	def activate(self, captain: Horatio, info=None):
		self.weapon.fire(captain.enemy_intel.location)
		return AttackInfo(info, self.weapon)
