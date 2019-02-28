from Ship import Ship
from Subroutines.States.Status import Status


class EnergyLevel(Status):
	own_ship: Ship
	enemy_ship: Ship
	range: int
	minmax = str
	
	def __init__(self, own_ship: Ship, enemy_ship: Ship, minmax: str):
		self.target = own_ship
		self.enemy_ship = enemy_ship
		self.minmax = minmax
	
	def test(self):
		result = False
		distance = self.calculate_distance(self.own_ship.location, self.enemy_ship.location)
		
		if self.minmax == "max":
			if distance <= self.range:
				result = True
		elif self.minmax == "min":
			if distance >= self.range:
				result = True
				
		return result
