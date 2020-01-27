from Components.Component import Component
from Models.Coordinates import Coordinates
from Models.Ship import Ship


class JumpDrive(Component):
	energy_cost: int
	
	def __init__(self, component_id: int, name: str, mass: int, energy_cost: int, repair_cost: int):
		self.component_id = component_id
		self.name = name
		self.mass = mass
		self.energy_cost = energy_cost
		self.repair_cost = repair_cost
		self.operational = True
	
	def get_stat_info(self):
		return {
			"id": self.component_id,
			"name": self.name,
			"mass": self.mass,
			"jump_cost": self.energy_cost
		}

	def jump_move(self, coord: Coordinates, ship: Ship):
		if ship.current_energy >= self.energy_cost:
			ship.location = coord
			ship.current_energy -= self.energy_cost
			return True
		else:
			return False
