from ....BLL.Horatio import Horatio
from ...Coordinates import Coordinates
from .Action import Action


class FireImpulse(Action):
	velocity_change: Coordinates
	
	def __init__(self, velocity_change: Coordinates):
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
