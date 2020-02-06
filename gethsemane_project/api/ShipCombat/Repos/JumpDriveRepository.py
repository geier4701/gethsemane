from typing import List

from api.models import JumpDriveModel


class JumpDriveRepository:
	def find_all(self) -> List[JumpDriveModel]:
		return JumpDriveModel.objects.all()

	def find_by_id(self, jump_drive_id: int) -> JumpDriveModel:
		return JumpDriveModel.objects.get(jump_drive_id=jump_drive_id)
	
	def find_by_name(self, jump_drive_name: str) -> JumpDriveModel:
		return JumpDriveModel.objects.get(name=jump_drive_name)
