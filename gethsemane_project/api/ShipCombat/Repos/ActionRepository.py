from typing import List

from api.models import ActionModel


class ActionRepository:
	def find_all(self) -> List[ActionModel]:
		return ActionModel.objects.all()
	
	def find_by_id(self, action_id: int) -> ActionModel:
		return ActionModel.objects.get(action_id=action_id)
	
	def find_by_name(self, action_name: str) -> ActionModel:
		return ActionModel.objects.get(name=action_name)
