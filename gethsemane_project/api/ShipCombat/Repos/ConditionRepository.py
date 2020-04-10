from typing import List

from api.models import ConditionModel


class ConditionRepository:
	def find_all(self, ) -> List[ConditionModel]:
		return ConditionModel.objects.all()
	
	def find_by_id(self, condition_id: int) -> ConditionModel:
		return ConditionModel.objects.get(condition_id=condition_id)
	
	def find_by_subroutine(self, subroutine_id: int) -> List[ConditionModel]:
		return ConditionModel.objects.filter(subroutine_id=subroutine_id)
	
	def save(self, condition_model: ConditionModel) -> None:
		condition_model.clean_fields(exclude='condition_id')
		condition_model.save()
