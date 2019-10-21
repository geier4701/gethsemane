from typing import List
from Subroutines.Actions import Action
from Subroutines.Conditions import Condition


class Subroutine:
	subroutine_id: int
	name: str
	ship_id: int
	priority: int
	conditions: List[Condition]
	actions: List[Action]
	
	def __init__(self, subroutine_id, name, ship_id, priority, conditions, actions):
		self.name = name
		self.subroutine_id = subroutine_id
		self.ship_id = ship_id
		self.priority = priority
		self.conditions = conditions
		self.actions = actions
