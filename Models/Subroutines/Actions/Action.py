from abc import ABC, abstractmethod


class Action(ABC):
	
	@abstractmethod
	def activate(self, arg):
		pass
