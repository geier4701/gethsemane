from api.ShipCombat.BLL.Horatio import Horatio
from api.ShipCombat.Models.Coordinates import Coordinates
from api.ShipCombat.Models.Subroutines.Actions.Action import Action


class FireImpulse(Action):
	name = "FireImpulse"
	velocity_change: Coordinates
	
	def __init__(self, action_id: int, velocity_change: Coordinates):
		self.action_id = action_id
		self.velocity_change = velocity_change
	
	def activate(self, captain: Horatio, info=None):
		if captain.own_ship.current_energy >= captain.own_ship.impulse_engine.energy_cost:
			captain.own_ship.current_energy -= captain.own_ship.impulse_engine.energy_cost
			captain.own_ship.location.speed[0] = captain.own_ship.location.speed[0] + self.velocity_change.speed[0]
			captain.own_ship.location.speed[1] = captain.own_ship.location.speed[1] + self.velocity_change.speed[1]
			captain.own_ship.location.speed[2] = captain.own_ship.location.speed[2] + self.velocity_change.speed[2]
			return True
		else:
			return False
