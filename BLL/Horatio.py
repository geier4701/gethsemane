from Ship import Ship
from Subroutines.Actions import Action


class Horatio:
	subroutines: []
	own_ship: Ship
	last_action: []
	enemy_ship: Ship
	
	def __init__(self, ship):
		self.own_ship = ship
		self.subroutines = ship.subroutines
	
	def command(self):
		self.subroutines.sort(self, self.subroutines.priority)
		for subroutine in self.subroutines:
			engage = True
			for condition in subroutine.conditions:
				if not condition.test(self.own_ship, self.enemy_ship):
					engage = False
			
				if engage:
					self.last_action = subroutine.actions
					return subroutine.actions
		
		return self.last_action
