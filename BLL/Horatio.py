from Ship import Ship
from Subroutines.Actions import Action


class Horatio:
	subroutines: []
	ship: Ship
	last_action: []
	
	def __init__(self, ship):
		self.ship = ship
		self.subroutines = ship.subroutines
	
	def command(self):
		self.subroutines.sort(self, self.subroutines.priority)
		for subroutine in self.subroutines:
			engage = True
			for condition in subroutine.conditions:
				if not condition:
					engage = False
			
			if engage:
				self.last_action = subroutine.actions
				# SHOULD PROBABLY PERFORM ACTION AND THEN SEND IT TO GAME MANAGER TO UPDATE GAME STATE
				return subroutine.actions
		
		return self.last_action
