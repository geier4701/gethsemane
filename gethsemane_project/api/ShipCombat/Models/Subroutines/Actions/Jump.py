from ....BLL.Horatio import Horatio
from .Action import Action
from ...Components.JumpDrive import JumpDrive


class Jump(Action):
	name = "Jump"
	jump_drive: JumpDrive
	
	def activate(self, captain: Horatio, info=None):
		if captain.own_ship.current_energy >= captain.own_ship.impulse_engine.energy_cost:
			captain.own_ship.current_energy -= captain.own_ship.impulse_engine.energy_cost
			captain.own_ship.location.speed[0] = captain.own_ship.location.speed[0] + info.location[0]
			captain.own_ship.location.speed[1] = captain.own_ship.location.speed[1] + info.location[1]
			captain.own_ship.location.speed[2] = captain.own_ship.location.speed[2] + info.location[2]
			return True
		else:
			return False
