from abc import ABC, abstractmethod
from typing import List
from gethsemane_project.ShipCombat.Models.Subroutines.Subroutine import Subroutine


class SubroutineRepository(ABC):
	@abstractmethod
	def get_subroutines(self, controlling_ship_id: int) -> List[Subroutine]:
		pass
	
	@abstractmethod
	def get_subroutine(self, subroutine_id: int) -> Subroutine:
		pass
