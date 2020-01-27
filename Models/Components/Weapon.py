from Components.Ammunition import AmmunitionType
from Components.Component import Component


class Weapon(Component):
	range: int
	damage: int
	ammunition_type: AmmunitionType
	munition_velocity: int
	energy_cost: int
	operational: bool
	
	def __init__(self, component_id: int, name: str, mass: int, energy_cost: int, repair_cost: int, damage: int, munition_velocity: int, ammunition_type: AmmunitionType):
		self.component_id = component_id
		self.name = name
		self.mass = mass
		self.energy_cost = energy_cost
		self.repair_cost = repair_cost
		self.damage = damage
		self.munition_velocity = munition_velocity
		self.ammunition_type = ammunition_type
		self.operational = True
	
	def get_stat_info(self):
		pass
