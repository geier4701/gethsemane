from enum import Enum


class TargetShip(Enum):
	SELF = 1
	ENEMY = 2


class Condition:
	target: TargetShip
	state: []
