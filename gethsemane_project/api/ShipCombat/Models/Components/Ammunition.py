from enum import IntEnum

from .Component import Component


class DamageType(IntEnum):
	ENERGY = 0
	EXPLOSIVE = 1
	IMPACT = 2
	EWAR = 3


class AmmunitionType(IntEnum):
	CRYSTAL = 0
	MISSILE = 1
	RAIL = 2
	ELECTRIC = 3


class Ammunition(Component):
	damage_type: DamageType
	ammunition_type: AmmunitionType
	remaining_ammo: int
	
	def __init__(self, component_id: int, name: str, mass: int, repair_cost: int, damage_type: DamageType, ammunition_type: AmmunitionType, remaining_ammo: int):
		self.component_id = component_id
		self.name = name
		self.mass = mass
		self.repair_cost = repair_cost
		self.damage_type = damage_type
		self.ammunition_type = ammunition_type
		self.remaining_ammo = remaining_ammo
		self.operational = True
	
	def get_stat_info(self):
		pass
