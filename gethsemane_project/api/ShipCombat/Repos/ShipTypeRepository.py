from typing import List

from api.models import ShipTypeModel


class ShipTypeRepository:
	def find_by_id(self, ship_type_id: int) -> ShipTypeModel:
		return ShipTypeModel.objects.get(ship_type_id=ship_type_id)
	
	def find_by_name(self, ship_type_name: int) -> ShipTypeModel:
		return ShipTypeModel.objects.get(name=ship_type_name)
	
	def find_by_character_id(self, character_id: int) -> List[ShipTypeModel]:
		return ShipTypeModel.objects.filter(character_id=character_id)
