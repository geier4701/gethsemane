from api.ShipCombat.BLL.Horatio import Horatio
from api.ShipCombat.Models.Subroutines.Actions.Action import Action


class Jump(Action):
	name = "Jump"
	jump_drive_name: str
	
	def __init__(self, action_id: int, jump_drive_name: str):
		self.action_id = action_id
		self.jump_drive_name = jump_drive_name
	
	def activate(self, captain: Horatio, info=None):
		jump_drive = captain.own_ship.get_components()[self.jump_drive_name]
		
		if captain.own_ship.current_energy >= jump_drive.energy_cost:
			captain.own_ship.current_energy -= jump_drive.energy_cost
			captain.own_ship.location.speed[0] = captain.own_ship.location.speed[0] + info.location[0]
			captain.own_ship.location.speed[1] = captain.own_ship.location.speed[1] + info.location[1]
			captain.own_ship.location.speed[2] = captain.own_ship.location.speed[2] + info.location[2]
			return True
		else:
			return False
