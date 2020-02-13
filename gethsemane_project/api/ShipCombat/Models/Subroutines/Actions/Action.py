from abc import ABC, abstractmethod
from enum import Enum

from api.ShipCombat.BLL.Horatio import Horatio


class AvailableActions(Enum):
	REPAIR = 'Attempt Repairs'
	DELAY = 'Delay'
	FIRE_IMPULSE = 'Fire Impulse Engines'
	FIRE_WEAPON = 'Fire Weapon'
	JUMP = 'Jump'
	SCAN = 'Scan'


class Action(ABC):
	action_id: int
	name: str
	
	@abstractmethod
	def activate(self, captain: Horatio, info=None):
		pass
