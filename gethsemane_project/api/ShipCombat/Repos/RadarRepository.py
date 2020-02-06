from typing import List

from api.models import RadarModel


class RadarRepository:
	def find_all(self) -> List[RadarModel]:
		return RadarModel.objects.all()
	
	def find_by_id(self, radar_id: int) -> RadarModel:
		return RadarModel.objects.get(radar_id=radar_id)
	
	def find_by_name(self, computer_name: str) -> RadarModel:
		return RadarModel.objects.get(name=computer_name)
