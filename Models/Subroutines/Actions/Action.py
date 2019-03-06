from abc import ABC, abstractmethod


class Action(ABC):
	name: str
	
	@abstractmethod
	def activate(self, ship, arg):
		pass
