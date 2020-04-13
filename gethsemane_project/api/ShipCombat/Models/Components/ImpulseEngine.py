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
