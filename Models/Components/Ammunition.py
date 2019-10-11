from enum import Enum
from Components.Component import Component


class DamageType(Enum):
	ENERGY: 0
	EXPLOSIVE: 1
	IMPACT: 2
	EWAR: 3


class Ammunition(Component):
	damage_type: DamageType
	
	def __init__(self, component_id: int, name: str, mass: int, repair_cost: int, damage_type: DamageType):
		self.component_id = component_id
		self.name = name
		self.mass = mass
		self.repair_cost = repair_cost
		self.damage_type = damage_type
		self.operational = True
	
	def get_stat_info(self):
		pass
