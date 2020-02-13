from api.ShipCombat.BLL.Horatio import Horatio
from api.ShipCombat.Models.AttackInfo import AttackInfo
from api.ShipCombat.Models.Components.Weapon import Weapon
from api.ShipCombat.Models.Subroutines.Actions.Action import Action


class FireWeapon(Action):
	name = "FireWeapon"
	weapon_name: str
	attack_info: AttackInfo
	ammunition_name: str
	
	def __init__(self, action_id: int, weapon_name: str, ammunition_name: str):
		self.action_id = action_id
		self.weapon_name = weapon_name
		self.ammunition_name = ammunition_name
	
	def activate(self, captain: Horatio, info=None):
		weapon: Weapon
		weapon = captain.own_ship.get_components()[self.weapon_name]
		ammo_to_check = captain.own_ship.get_components()[self.ammunition_name]
		
		ammo_to_use = None
		for ammo in ammo_to_check:
			if ammo.remaining_ammo > 0:
				ammo_to_use = ammo
				break
		
		return AttackInfo(info, weapon, ammo_to_use)
