from Component import Component
from Coordinates import Coordinates


class Weapon(Component):
	range: int
	damage_type: str
	missile_velocity: int
	energy_cost: int
	munition_type: str
	ammunition: int
	operational: bool
	
	def __init__(self, id: int, name: str, damage_type: str, mass: int, missile_velocity: int, energy_cost: int, munition_type: str, ammunition: 0):
		self.id = id
		self. name = name
		self. damage_type = damage_type
		self.mass = mass
		self.missile_velocity = missile_velocity
		self.energy_cost = energy_cost
		self.munition_type = munition_type
		self.ammunition = ammunition
		self.operational = True
	
	def fire(self, coord: Coordinates):
		pass

	def get_stat_info(self):
		pass
