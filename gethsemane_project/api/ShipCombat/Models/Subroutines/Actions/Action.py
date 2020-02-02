from abc import ABC, abstractmethod

from ....BLL.Horatio import Horatio


class Action(ABC):
	name: str
	
	@abstractmethod
	def activate(self, captain: Horatio, info=None):
		pass
