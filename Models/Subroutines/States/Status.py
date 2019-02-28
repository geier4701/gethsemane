import math
from abc import ABC, abstractmethod

from Coordinates import Coordinates


class Status(ABC):
	# TAKES SHIP AND/OR COMPONENT
	# EITHER HEALTH, DISTANCE, AMMUNITION, ENERGY LEVEL, OR TURNS(?) SINCE LAST SCAN
	@abstractmethod
	def test(self):
		pass
	
	@staticmethod
	def calculate_distance(coord1: Coordinates, coord2: Coordinates):
		x = coord2.location[0] - coord1.location[0]
		y = coord2.location[1] - coord1.location[1]
		z = coord2.location[2] - coord1.location[2]
		return math.sqrt((x * x) + (y * y) + (z * z))
