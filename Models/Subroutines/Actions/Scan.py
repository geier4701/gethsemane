from BLL.Horatio import Horatio
from Radar import Radar
from Subroutines.Actions.Action import Action


class Scan(Action):
	name = "Scan"
	radar: Radar
	
	def __init__(self, radar: Radar):
		self.radar = radar
	
	def activate(self, captain: Horatio, info=None):
		if captain.own_ship.current_energy >= captain.own_ship.impulse_engine.energy_cost:
			captain.own_ship.current_energy -= captain.own_ship.impulse_engine.energy_cost
			return True
		else:
			return False
