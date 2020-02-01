import math
from abc import ABC, abstractmethod
from enum import IntEnum
from typing import List
from gethsemane_project.ShipCombat.Models.Components.Ammunition import AmmunitionType, Ammunition
from gethsemane_project.ShipCombat.Models.Coordinates import Coordinates
from gethsemane_project.ShipCombat.Models.Ship import Ship


class Target(IntEnum):
	SELF = 0
	ENEMY = 1


class Condition(ABC):
	at_least: int
	at_most: int
	target: Target
	
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
	
	@abstractmethod
	def test(self, own_ship: Ship, enemy_ship: Ship) -> bool:
		pass
	
	@staticmethod
	def calculate_distance(coord1: Coordinates, coord2: Coordinates) -> float:
		x = coord2.location[0] - coord1.location[0]
		y = coord2.location[1] - coord1.location[1]
		z = coord2.location[2] - coord1.location[2]
		return math.sqrt((x * x) + (y * y) + (z * z))
	
	@staticmethod
	def get_ammunition(ammo_type: AmmunitionType, ammunitions: List[Ammunition]) -> List[Ammunition]:
		to_test = []
		for ammo in ammunitions:
			if ammo.ammunition_type is ammo_type:
				to_test.append(ammo)
		
		return to_test
