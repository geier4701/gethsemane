from typing import List

from api.models import ComputerModel


class ComputerRepository:
	def find_all(self) -> List[ComputerModel]:
		return ComputerModel.objects.all()
	
	def find_by_id(self, computer_id: int) -> ComputerModel:
		return ComputerModel.objects.get(computer_id=computer_id)
	
	def find_by_name(self, computer_name: str) -> ComputerModel:
		return ComputerModel.objects.get(name=computer_name)
