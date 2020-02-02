from ....BLL.Horatio import Horatio
from ...Components.Component import Component
from .Action import Action


class AttemptRepairs(Action):
	name = "AttemptRepairs"
	component: Component
	
	def __init__(self, component: Component):
		self.component = component
	
	def activate(self, captain: Horatio, info=None):
		if captain.own_ship.current_energy >= self.component.repair_cost:
			captain.own_ship.current_energy -= self.component.repair_cost
			self.component.enable()
			return True
		else:
			return False