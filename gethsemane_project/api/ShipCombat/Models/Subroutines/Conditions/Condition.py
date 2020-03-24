import math
from abc import ABC, abstractmethod
from enum import IntEnum
from typing import Optional

from api.ShipCombat.Models.Coordinates import Coordinates


class Target(IntEnum):
	SELF = 0
	ENEMY = 1


class Condition(ABC):
	at_least: Optional[int]
	at_most: Optional[int]
	target: Target
	name: str
	
	def compare(self, ships_value: int) -> bool:
		at_least_result = False
		at_most_result = False
		
		if self.at_most is None:
			at_most_result = True
		else:
			if ships_value <= self.at_most:
				at_most_result = True
		
		if self.at_least is None:
			at_least_result = True
		else:
			if ships_value >= self.at_least:
				at_least_result = True
		
		return at_least_result and at_most_result
	
	@staticmethod
	def calculate_distance(coord1: Coordinates, coord2: Coordinates) -> float:
		x = coord2.location[0] - coord1.location[0]
		y = coord2.location[1] - coord1.location[1]
		z = coord2.location[2] - coord1.location[2]
		return math.sqrt((x * x) + (y * y) + (z * z))
	
	@staticmethod
	def find_desired_coord(desired_distance: int) -> Coordinates:
		# TODO: FIGURE OUT ALGORITHM TO PLACE SHIP AT A DESIRED DISTANCE FROM ENEMY SHIP
		pass
