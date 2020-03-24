from api.ShipCombat.Models.Components.Component import Component
from api.models import JumpDriveModel


class JumpDrive(Component):
	energy_cost: int
	
	def __init__(self, model: JumpDriveModel):
		self.component_id = model.jump_drive_id
		self.name = model.name
		self.mass = model.mass
		self.energy_cost = model.energy_cost
		self.repair_cost = model.repair_cost
		self.operational = True
