from typing import List

from api.models import SubroutineModel


class SubroutineRepository:
	@staticmethod
	def find_by_id(subroutine_id: int) -> SubroutineModel:
		return SubroutineModel.objects.get(subroutine_id=subroutine_id)
	
	@staticmethod
	def find_by_ship_id(ship_id: int) -> List[SubroutineModel]:
		return SubroutineModel.objects.filter(ship_id=ship_id)
