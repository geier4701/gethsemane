from enum import Enum
from Components.Component import Component


class AmmunitionType(Enum):
	CRYSTAL: 0
	MISSILE: 1
	RAIL: 2
	ELECTRIC: 3


class Weapon(Component):
	range: int
	damage: int
	ammunition_type: AmmunitionType
	munition_velocity: int
	energy_cost: int
	operational: bool
	
	def __init__(self, component_id: int, name: str, mass: int, repair_cost: int, damage: int, ammunition_type: AmmunitionType,
				munition_velocity: int, energy_cost: int):
		self.component_id = component_id
		self.name = name
		self.mass = mass
		self.repair_cost = repair_cost
		self.damage = damage
		self.ammunition_type = ammunition_type
		self.munition_velocity = munition_velocity
		self.energy_cost = energy_cost
		self.operational = True
	
	def get_stat_info(self):
		pass
