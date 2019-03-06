from Radar import Radar
from Ship import Ship
from Subroutines.Actions.Action import Action


class Scan(Action):
	name = "Scan"
	radar: Radar
	
	def activate(self, own_ship: Ship, enemy_ship: Ship):
		if own_ship.current_energy >= own_ship.impulse_engine.energy_cost:
			own_ship.current_energy -= own_ship.impulse_engine.energy_cost
			return True
		else:
			return False
