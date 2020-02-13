from api.ShipCombat.BLL.Horatio import Horatio
from api.ShipCombat.Models.Subroutines.Actions.Action import Action


class Scan(Action):
	name = "Scan"
	radar_name: str
	
	def __init__(self, action_id: int, radar_name: str):
		self.action_id = action_id
		self.radar_name = radar_name
	
	def activate(self, captain: Horatio, info=None):
		radar = captain.own_ship.get_components()[self.radar_name]
		
		if captain.own_ship.current_energy >= radar.energy_cost:
			captain.own_ship.current_energy -= radar.energy_cost
			return True
		else:
			return False
