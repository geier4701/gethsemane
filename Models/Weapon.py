from Component import Component


class Weapon(Component):
	id: int
	name: str
	range: int
	damage_type: str
	mass: int
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
	
	def disable(self):
		self.operational = False
	
	def enable(self):
		self.operational = True
	
	def fire(self):
		pass
