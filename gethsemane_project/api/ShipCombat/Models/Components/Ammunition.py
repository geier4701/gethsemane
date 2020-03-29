from enum import IntEnum

from api.ShipCombat.Models.Components.Component import Component
from api.models import AmmunitionModel


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
	
	def __init__(self, model: AmmunitionModel):
		self.component_id = model.ammunition_id
		self.name = model.name
		self.mass = model.mass
		self.repair_cost = model.repair_cost
		self.damage_type = DamageType(model.damage_type)
		self.ammunition_type = AmmunitionType(int(model.ammunition_type))
		self.remaining_ammo = model.max_ammunition
		self.operational = True
