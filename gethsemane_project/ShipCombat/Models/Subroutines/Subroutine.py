from typing import List

from gethsemane_project.ShipCombat.Models.Subroutines.Actions.Action import Action
from gethsemane_project.ShipCombat.Models.Subroutines.Conditions.Condition import Condition


class Subroutine:
	subroutine_id: int
	ship_id: int
	priority: int
	conditions: List[Condition]
	actions: List[Action]
	
	def __init__(self, subroutine_id, ship_id, priority, conditions, actions):
		self.subroutine_id = subroutine_id
		self.ship_id = ship_id
		self.priority = priority
		self.conditions = conditions
		self.actions = actions
