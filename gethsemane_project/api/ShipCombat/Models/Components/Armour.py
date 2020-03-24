from enum import IntEnum

from api.ShipCombat.Models.Components.Component import Component
from api.models import ArmourModel


class ArmourType(IntEnum):
	REFLECTIVE = 0
	REACTIVE = 1
	ABLATIVE = 2
	# CHECK OUT ELECTRICALLY CHARGED ARMOUR ON WIKIPEDIA
	CHARGED = 3


class Armour(Component):
	armour_type: ArmourType
	
	def __init__(self, model: ArmourModel):
		self.component_id = model.armour_id
		self.name = model.name
		self.mass = model.mass
		self.repair_cost = model.repair_cost
		self.armour_type = ArmourType(model.armour_type)
		self.operational = True
	
	# ARMOUR WILL HAVE STRAIGHT MASS REMOVED INSTEAD OF HALVING HP OR LOWERING DAMAGE
	# ONLY ELECTRICAL ARMOUR WILL BE REPAIRABLE
