from abc import ABC
from enum import Enum


class TrackingStyle(Enum):
	ACTIVE = 1
	PASSIVE = 2


class RadarClass(ABC):
	tracking_style: TrackingStyle
	power_consumption: int
	mass: int
	
	def pulse(self):
		# CHECK ENERGY
		# DRAIN ENERGY
		# PING OTHER SHIP FOR POSITION
		pass
