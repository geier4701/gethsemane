import math
from abc import ABC, abstractmethod
from enum import Enum
from Coordinates import Coordinates
from Ship import Ship


class Target(Enum):
	SELF: 0
	ENEMY: 1


class Condition(ABC):
	at_least: int
	at_most: int
	target: Target
	
	@abstractmethod
	def test(self, own_ship: Ship, enemy_ship: Ship):
		pass
	
	@staticmethod
	def calculate_distance(coord1: Coordinates, coord2: Coordinates):
		x = coord2.location[0] - coord1.location[0]
		y = coord2.location[1] - coord1.location[1]
		z = coord2.location[2] - coord1.location[2]
		return math.sqrt((x * x) + (y * y) + (z * z))
