from abc import ABC, abstractmethod


class Component(ABC):
	id: int
	name: str
	mass: int
	
	@abstractmethod
	def get_stat_info(self):
		pass
