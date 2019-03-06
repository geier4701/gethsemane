from Coordinates import Coordinates
from JumpDrive import JumpDrive
from Ship import Ship
from Subroutines.Actions.Action import Action


class Jump(Action):
	name = "Jump"
	jump_drive: JumpDrive
	
	def activate(self, ship: Ship, coord: Coordinates):
		if ship.current_energy >= ship.impulse_engine.energy_cost:
			ship.current_energy -= ship.impulse_engine.energy_cost
			ship.location.speed[0] = ship.location.speed[0] + coord.location[0]
			ship.location.speed[1] = ship.location.speed[1] + coord.location[1]
			ship.location.speed[2] = ship.location.speed[2] + coord.location[2]
			return True
		else:
			return False
