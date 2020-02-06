from typing import List

from api.models import ImpulseEngineModel


class ImpulseEngineRepository:
	def find_all(self) -> List[ImpulseEngineModel]:
		return ImpulseEngineModel.objects.all()
	
	def find_by_id(self, impulse_engine_id: int) -> ImpulseEngineModel:
		return ImpulseEngineModel.objects.get(impulse_engine_id=impulse_engine_id)
	
	def find_by_name(self, impulse_engine_name: str) -> ImpulseEngineModel:
		return ImpulseEngineModel.objects.get(name=impulse_engine_name)
