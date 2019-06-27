from BLL.Horatio import Horatio
from Component import Component
from Subroutines.Actions.Action import Action


class AttemptRepairs(Action):
	name = "AttemptRepairs"
	component: Component
	
	def __init__(self, component: Component):
		self.component = component
	
	def activate(self, captain: Horatio):
		if captain.own_ship.current_energy >= self.component.repair_cost:
			captain.own_ship.current_energy -= self.component.repair_cost
			self.component.enable()
