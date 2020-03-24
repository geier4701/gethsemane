from api.ShipCombat.Models.Components.Component import Component
from api.models import ImpulseEngineModel


class ImpulseEngine(Component):
	max_accel: int
	energy_cost: int
	
	def __init__(self, model: ImpulseEngineModel):
		self.component_id = model.impulse_engine_id
		self.name = model.name
		self.mass = model.mass
		self.energy_cost = model.energy_cost
		self.repair_cost = model.repair_cost
		self.max_accel = model.max_accel
		self.operational = True

# a few ways to go about it. 1. no generating power. All  battery operated ships, ensuring that they need to manage
# energy as a resource. 2. power generation tied to ship class. You don't get to pick how much power is generated a
# turn, but you can devote extra weight to batteries if you want. 3. You must pick different power plants depending on
# how much power you want to generate each turn. or,4. no batteries, only a generation amount. You get your power
# every turn and that's it, with no way to store it for later. Works with either pick a power plant or tied to ship
# class methods
