from api.ShipCombat.Models.Subroutines.Actions.Action import Action


class FireWeapon(Action):
	name = "FireWeapon"
	weapon_name: str
	ammunition_name: str
	
	def __init__(self, action_id: int, weapon_name: str, ammunition_name: str):
		self.action_id = action_id
		self.weapon_name = weapon_name
		self.ammunition_name = ammunition_name
