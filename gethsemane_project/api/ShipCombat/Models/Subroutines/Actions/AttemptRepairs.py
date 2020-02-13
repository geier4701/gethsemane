from api.ShipCombat.BLL.Horatio import Horatio
from api.ShipCombat.Models.Subroutines.Actions.Action import Action


class AttemptRepairs(Action):
	name = "AttemptRepairs"
	component_name: str
	
	def __init__(self, action_id: int, component_name: str):
		self.action_id = action_id
		self.component_name = component_name
	
	def activate(self, captain: Horatio, info=None):
		component = captain.own_ship.get_components()[self.component_name]
		if captain.own_ship.current_energy >= component.repair_cost:
			captain.own_ship.current_energy -= component.repair_cost
			component.enable()
			return True
		else:
			return False
