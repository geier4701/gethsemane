from ....BLL.Horatio import Horatio
from ...AttackInfo import AttackInfo
from ...Components.Weapon import Weapon
from .Action import Action
from ..Conditions.Condition import Condition


class FireWeapon(Action):
	name = "FireWeapon"
	weapon: Weapon
	attack_info: AttackInfo
	
	def __init__(self, weapon: Weapon):
		self.weapon = weapon
	
	def activate(self, captain: Horatio, info=None):
		ammo_to_check = Condition.get_ammunition(self.weapon.ammunition_type, captain.own_ship.ammunitions)
		
		ammo_to_use = None
		for ammo in ammo_to_check:
			if ammo.remaining_ammo > 0:
				ammo_to_use = ammo
				break
		
		return AttackInfo(info, self.weapon, ammo_to_use)
