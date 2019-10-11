from enum import Enum
from Components.Component import Component


class ArmourType(Enum):
	REFLECTIVE: 0
	REACTIVE: 1
	ABLATIVE: 2
	# CHECK OUT ELECTRICALLY CHARGED ARMOUR ON WIKIPEDIA
	CHARGED: 3


class Armour(Component):
	armour_type: ArmourType
	
	def __init__(self, component_id: int, name: str, mass: int, repair_cost: int, armour_type: ArmourType):
		self.component_id = component_id
		self.name = name
		self.mass = mass
		self.repair_cost = repair_cost
		self.armour_type = armour_type
		self.operational = True
	
	def get_stat_info(self):
		pass
	
	# ARMOUR WILL HAVE STRAIGHT MASS REMOVED INSTEAD OF HAVING HP OR LOWERING DAMAGE
	# ONLY ELECTRICAL ARMOUR WILL BE REPAIRABLE
