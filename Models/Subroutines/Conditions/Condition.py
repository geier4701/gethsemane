import math
from abc import ABC, abstractmethod
from enum import Enum
from typing import List
from Components import Ammunition
from Components.Weapon import AmmunitionType
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
