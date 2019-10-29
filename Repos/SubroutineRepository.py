from abc import ABC, abstractmethod
from typing import List
from Subroutines import Subroutine


class SubroutineRepository(ABC):
	@abstractmethod
	def get_subroutines(self, controlling_ship_id: int) -> List[Subroutine]:
		pass
	
	@abstractmethod
	def get_subroutine(self, subroutine_id: int) -> Subroutine:
		pass
