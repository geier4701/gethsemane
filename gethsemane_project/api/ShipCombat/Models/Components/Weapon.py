from api.ShipCombat.Models.Components.Ammunition import AmmunitionType
from api.ShipCombat.Models.Components.Component import Component
from api.models import WeaponModel


class Weapon(Component):
	range: int
	damage: int
	ammunition_type: AmmunitionType
	munition_velocity: int
	energy_cost: int
	operational: bool
	has_fired: bool
	
	def __init__(self, model: WeaponModel):
		self.component_id = model.weapon_id
		self.name = model.name
		self.mass = model.mass
		self.energy_cost = model.energy_cost
		self.repair_cost = model.repair_cost
		self.damage = model.damage
		self.munition_velocity = model.munition_velocity
		self.ammunition_type = AmmunitionType(int(model.ammunition_type))
		self.operational = True
		self.has_fired = False
