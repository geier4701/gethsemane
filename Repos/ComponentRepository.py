from abc import ABC, abstractmethod
from typing import List

from Components import Component


class ComponentRepository(ABC):
	@abstractmethod
	def get_components_of_type(self, component_type: str) -> List[Component]:
		pass
	
	@abstractmethod
	def get_component(self, component_id: int, component_type: str) -> Component:
		pass
