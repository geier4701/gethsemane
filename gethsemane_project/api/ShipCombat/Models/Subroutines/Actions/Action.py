from abc import ABC, abstractmethod

from api.ShipCombat.BLL.Horatio import Horatio


class Action(ABC):
	action_id: int
	name: str
	
	@abstractmethod
	def activate(self, captain: Horatio, info=None):
		pass
