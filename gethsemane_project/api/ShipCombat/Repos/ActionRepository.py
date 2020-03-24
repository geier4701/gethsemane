from typing import List

from api.models import ActionModel


class ActionRepository:
	@staticmethod
	def find_all() -> List[ActionModel]:
		return ActionModel.objects.all()
	
	@staticmethod
	def find_by_id(action_id: int) -> ActionModel:
		return ActionModel.objects.get(action_id=action_id)
	
	@staticmethod
	def find_by_name(action_name: str) -> ActionModel:
		return ActionModel.objects.filter(name=action_name)
	
	@staticmethod
	def find_by_subroutine(subroutine_id: int) -> List[ActionModel]:
		return ActionModel.objects.filter(subroutines__subroutine_id=subroutine_id)
