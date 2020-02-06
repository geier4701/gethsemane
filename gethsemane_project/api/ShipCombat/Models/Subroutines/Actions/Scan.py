from api.ShipCombat.BLL.Horatio import Horatio
from api.ShipCombat.Models.Components.Radar import Radar
from api.ShipCombat.Models.Subroutines.Actions.Action import Action


class Scan(Action):
	name = "Scan"
	radar: Radar
	
	def __init__(self, action_id: int, radar: Radar):
		self.action_id = action_id
		self.radar = radar
	
	def activate(self, captain: Horatio, info=None):
		if captain.own_ship.current_energy >= captain.own_ship.impulse_engine.energy_cost:
			captain.own_ship.current_energy -= captain.own_ship.impulse_engine.energy_cost
			return True
		else:
			return False
