from typing import List

from api.models import SubroutineModel


class SubroutineRepository:
	def find_by_id(self, subroutine_id: int) -> SubroutineModel:
		return SubroutineModel.objects.get(subroutine_id=subroutine_id)
	
	def find_by_program_id(self, program_id: int) -> List[SubroutineModel]:
		return SubroutineModel.objects.filter(program_id=program_id)
	
	def save(self, subroutine_model: SubroutineModel) -> None:
		subroutine_model.clean_fields(exclude='subroutine_id')
		subroutine_model.save()
	
	def delete(self, subroutine_model: SubroutineModel) -> None:
		subroutine_model.delete()
