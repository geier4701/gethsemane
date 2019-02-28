from Models.Component import Component
from Models.Coordinates import Coordinates
from Models.Ship import Ship


class JumpDrive(Component):
	jump_cost: int
	
	def __init__(self, id: int, name: str, mass: int, jump_cost: int):
		self.id = id
		self.name = name
		self.mass = mass
		self.jump_cost = jump_cost
	
	def get_stat_info(self):
		return {
			"id": self.id,
			"name": self.name,
			"mass": self.mass,
			"jump_cost": self.jump_cost
		}

	def jump_move(self, coord: Coordinates, ship: Ship):
		if ship.current_energy >= self.jump_cost:
			ship.location = coord
			ship.current_energy -= self.jump_cost
			return True
		else:
			return False
