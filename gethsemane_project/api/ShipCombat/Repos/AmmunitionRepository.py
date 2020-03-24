from typing import List

from ...models import AmmunitionModel


class AmmunitionRepository:
	def find_all(self) -> List[AmmunitionModel]:
		return AmmunitionModel.objects.all()
	
	def find_by_id(self, jump_drive_id: int) -> AmmunitionModel:
		return AmmunitionModel.objects.get(ammunition_id=jump_drive_id)
	
	def find_by_name(self, jump_drive_name: str) -> AmmunitionModel:
		return AmmunitionModel.objects.get(name=jump_drive_name)
	
	def find_by_ship_id(self, ship_id: int) -> List[AmmunitionModel]:
		return AmmunitionModel.objects.filter(shipmodel__ship_id=ship_id)
