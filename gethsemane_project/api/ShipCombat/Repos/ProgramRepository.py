from typing import List

from api.models import ProgramModel


class ProgramRepository:
	def find_by_id(self, program_id: int) -> ProgramModel:
		return ProgramModel.objects.get(program_id=program_id)
	
	def find_by_character_id(self, character_id: int) -> List[ProgramModel]:
		return ProgramModel.objects.filter(character_id=character_id)
	
	def save(self, program_model: ProgramModel) -> None:
		program_model.clean_fields(exclude=['program_id', 'ship_id'])
		program_model.save()
