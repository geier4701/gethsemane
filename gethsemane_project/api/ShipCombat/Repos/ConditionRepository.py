from typing import List

from api.models import ConditionModel


class ConditionRepository:
	@staticmethod
	def find_all() -> List[ConditionModel]:
		return ConditionModel.objects.all()
	
	@staticmethod
	def find_by_id(condition_id: int) -> ConditionModel:
		return ConditionModel.objects.get(condition_id=condition_id)

	@staticmethod
	def find_by_subroutine(subroutine_id: int) -> List[ConditionModel]:
		return ConditionModel.objects.filter(subroutine__id=subroutine_id)
