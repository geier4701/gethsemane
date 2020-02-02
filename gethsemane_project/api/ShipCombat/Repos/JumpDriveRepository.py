from ..Models.Components.JumpDrive import JumpDrive
from ...models import JumpDriveModel


def getJumpDriveById(jump_drive_id: int) -> JumpDrive:
	jump_drive_model = JumpDriveModel.objects.get(jump_drive_id=jump_drive_id)
	return jump_drive_model


# class JumpDriveRepository:
# 	def getAllJumpDrives(self) -> List[JumpDrive]:
# 		jump_drive_models = JumpDriveModel.objects.all()
# 		return jump_drive_models
#
# 	def getJumpDriveById(self, jump_drive_id: int) -> JumpDrive:
# 		jump_drive_model = JumpDriveModel.objects.get(jump_drive_id=jump_drive_id)
# 		return jump_drive_model
