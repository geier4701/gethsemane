from api.ShipCombat.BLL.Horatio import Horatio
from api.ShipCombat.Models.Components.Component import Component
from api.ShipCombat.Models.Subroutines.Actions.Action import Action


class AttemptRepairs(Action):
	name = "AttemptRepairs"
	component: Component
	
	def __init__(self, action_id: int, component: Component):
		self.action_id = action_id
		self.component = component
	
	def activate(self, captain: Horatio, info=None):
		if captain.own_ship.current_energy >= self.component.repair_cost:
			captain.own_ship.current_energy -= self.component.repair_cost
			self.component.enable()
			return True
		else:
			return False
