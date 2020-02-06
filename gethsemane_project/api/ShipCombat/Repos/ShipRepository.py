from typing import List

from api.models import ShipModel


class ShipRepository:
	def find_all(self) -> List[ShipModel]:
		return ShipModel.objects.all()
	
	def find_by_id(self, ship_id: int) -> ShipModel:
		return ShipModel.objects.get(ship_id=ship_id)
	
	def find_by_name(self, ship_name: str) -> List[ShipModel]:
		return ShipModel.objects.filter(name=ship_name)
