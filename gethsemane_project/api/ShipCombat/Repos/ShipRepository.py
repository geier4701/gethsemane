from typing import List

from api.models import ShipModel


class ShipRepository:
	def find_all(self) -> List[ShipModel]:
		return ShipModel.objects.all()
	
	def find_by_id(self, ship_id: int) -> ShipModel:
		return ShipModel.objects.get(ship_id=ship_id)
	
	def find_by_name(self, ship_name: str) -> ShipModel:
		return ShipModel.objects.filter(name=ship_name)
	
	def find_by_user_and_name(self, user_name: str, ship_name: str):
		# THIS WILL TAKE OVER FIND_BY_NAME TO ALLOW FOR NON-UNIQUE NAMES
		pass
