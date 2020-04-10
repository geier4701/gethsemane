from typing import List

from api.models import ActionModel


class ActionRepository:
	def find_by_id(self, action_id: int) -> ActionModel:
		return ActionModel.objects.get(action_id=action_id)
	
	def find_by_name(self, action_name: str) -> ActionModel:
		return ActionModel.objects.filter(name=action_name)
	
	def find_by_subroutine(self, subroutine_id: int) -> List[ActionModel]:
		return ActionModel.objects.filter(subroutine_id=subroutine_id)
	
	def save(self, action_model: ActionModel) -> None:
		action_model.clean_fields(exclude='action_id')
		action_model.save()
