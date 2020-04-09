from typing import List

from api.models import ArmourModel


class ArmourRepository:
	def find_all(self) -> List[ArmourModel]:
		return ArmourModel.objects.all()
	
	def find_by_id(self, armour_id: int) -> ArmourModel:
		return ArmourModel.objects.get(armour_id=armour_id)
	
	def find_by_name(self, armour_name: str) -> ArmourModel:
		return ArmourModel.objects.get(name=armour_name)
	
	def find_by_character_id(self, character_id: int) -> List[ArmourModel]:
		return ArmourModel.objects.filter(character_id=character_id)
