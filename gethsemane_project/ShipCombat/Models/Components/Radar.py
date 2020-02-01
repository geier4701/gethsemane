from enum import IntEnum
from gethsemane_project.ShipCombat.Models.Components.Component import Component
from gethsemane_project.ShipCombat.Models.Coordinates import Coordinates


class TrackingStyle(IntEnum):
	PASSIVE = 0
	ACTIVE = 1


class Radar(Component):
	tracking_style: TrackingStyle
	energy_cost: int
	enemy_coord: Coordinates
	
	def __init__(self, component_id: int, name: str, mass: int, energy_cost: int, repair_cost: int, tracking_style: TrackingStyle):
		self.component_id = component_id
		self.name = name
		self.mass = mass
		self.energy_cost = energy_cost
		self.repair_cost = repair_cost
		self.tracking_style = tracking_style
		self.operational = True
		self.enemy_coord = Coordinates(0, 0, 0)
	
	def get_stat_info(self):
		return {
			'id': self.component_id,
			'name': self.name,
			'mass': self.mass,
			'tracking_style': self.tracking_style,
			'energy_cost': self.energy_cost
		}
