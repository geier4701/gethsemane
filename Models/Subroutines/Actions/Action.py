from abc import ABC, abstractmethod

from BLL.Horatio import Horatio
from Ship import Ship


class Action(ABC):
	name: str
	
	@abstractmethod
	def activate(self, captain: Horatio):
		pass
