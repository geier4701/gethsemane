from Coordinates import Coordinates
from Ship import Ship
from Subroutines.Actions.Action import Action


class FireImpulse(Action):
	def activate(self, ship: Ship, velocity_change: Coordinates):
		if ship.current_energy >= ship.impulse_engine.energy_cost:
			ship.current_energy -= ship.impulse_engine.energy_cost
			ship.location.speed[0] = ship.location.speed[0] + velocity_change.speed[0]
			ship.location.speed[1] = ship.location.speed[1] + velocity_change.speed[1]
			ship.location.speed[2] = ship.location.speed[2] + velocity_change.speed[2]
			return True
		else:
			return False
