from Ship import Ship


class Horatio:
	subroutines: []
	ship: Ship
	
	def __init__(self, subroutines, ship):
		self.subroutines = subroutines
		self.ship = ship
	
	def command(self):
		self.subroutines.sort(self, self.subroutines.priority)
		for subroutine in self.subroutines:
			engage = True
			for condition in subroutine.Conditions:
				if not condition:
					engage = False
			
			if engage:
				return subroutine.Actions
