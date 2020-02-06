from api.ShipCombat.BLL.Horatio import Horatio
from api.ShipCombat.Models.AttackInfo import AttackInfo
from api.ShipCombat.Models.Components.Weapon import Weapon
from api.ShipCombat.Models.Subroutines.Actions.Action import Action
from api.ShipCombat.Models.Subroutines.Conditions.Condition import Condition


class FireWeapon(Action):
	name = "FireWeapon"
	weapon: Weapon
	attack_info: AttackInfo
	
	def __init__(self, action_id: int, weapon: Weapon):
		self.action_id = action_id
		self.weapon = weapon
	
	def activate(self, captain: Horatio, info=None):
		ammo_to_check = Condition.get_ammunition(self.weapon.ammunition_type, captain.own_ship.ammunitions)
		
		ammo_to_use = None
		for ammo in ammo_to_check:
			if ammo.remaining_ammo > 0:
				ammo_to_use = ammo
				break
		
		return AttackInfo(info, self.weapon, ammo_to_use)
