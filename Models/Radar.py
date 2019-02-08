from enum import Enum
from Component import Component


class TrackingStyle(Enum):
	ACTIVE = 1
	PASSIVE = 2


class Radar(Component):
	tracking_style: TrackingStyle
	power_consumption: int
	
	def __init__(self, id: int, name: str, mass: int, tracking_style: TrackingStyle, power_consumption: int):
		self.id = id
		self.name = name
		self.mass = mass
		self.tracking_style = tracking_style
		self.power_consumption = power_consumption
	
	def pulse(self):
		# CHECK ENERGY
		# DRAIN ENERGY
		# PING OTHER SHIP FOR POSITION
		pass
