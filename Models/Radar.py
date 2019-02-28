from enum import Enum

from Coordinates import Coordinates
from Models.Component import Component


class TrackingStyle(Enum):
	ACTIVE = 1
	PASSIVE = 2


class Radar(Component):
	tracking_style: TrackingStyle
	power_consumption: int
	enemy_coord: int
	
	def __init__(self, id: int, name: str, mass: int, tracking_style: TrackingStyle, power_consumption: int):
		self.id = id
		self.name = name
		self.mass = mass
		self.tracking_style = tracking_style
		self.power_consumption = power_consumption
		self.enemy_coord = Coordinates(0, 0, 0)
	
	def pulse(self):
		# CHECK ENERGY
		# DRAIN ENERGY
		# PING OTHER SHIP FOR POSITION
		pass
	
	def get_stat_info(self):
		return {
			'id': self.id,
			'name': self.name,
			'mass': self.mass,
			'tracking_style': self.tracking_style,
			'power_consumption': self.power_consumption
		}
