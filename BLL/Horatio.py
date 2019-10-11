from Ship import Ship
from Subroutines import Subroutine
from typing import List


class Horatio:
	subroutines: List[Subroutine]
	own_ship: Ship
	last_action: list
	enemy_intel: Ship
	
	def __init__(self, ship: Ship):
		self.own_ship = ship
		self.subroutines = ship.subroutines
		self.enemy_intel = Ship()
	
	def command(self):
		self.subroutines.sort(key=lambda sub: subroutine.priority)
		actions_to_take = list
		for subroutine in self.subroutines:
			make_it_so = True
			for condition in subroutine.conditions:
				if not condition.test(self.own_ship, self.enemy_intel):
					make_it_so = False
			
			if make_it_so:
				self.last_action = subroutine.actions
				actions_to_take = subroutine.actions
		
		if not actions_to_take:
			actions_to_take = self.last_action
		
		return actions_to_take
