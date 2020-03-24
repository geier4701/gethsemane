from enum import IntEnum

from api.ShipCombat.Models.Coordinates import Coordinates
from api.ShipCombat.Models.Components.Component import Component
from api.models import RadarModel


class TrackingStyle(IntEnum):
	PASSIVE = 0
	ACTIVE = 1


class Radar(Component):
	tracking_style: TrackingStyle
	energy_cost: int
	enemy_coord: Coordinates
	
	def __init__(self, model: RadarModel):
		self.component_id = model.radar_id
		self.name = model.name
		self.mass = model.mass
		self.energy_cost = model.energy_cost
		self.repair_cost = model.repair_cost
		self.tracking_style = TrackingStyle(model.tracking_style)
		self.operational = True
		self.enemy_coord = Coordinates(0, 0, 0, 0, 0, 0)
