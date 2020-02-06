from typing import List

from api.models import WeaponModel


class WeaponRepository:
	def find_all(self) -> List[WeaponModel]:
		return WeaponModel.objects.all()
	
	def find_by_id(self, weapon_id: int) -> WeaponModel:
		return WeaponModel.objects.get(weapon_id=weapon_id)
	
	def find_by_name(self, weapon_name: str) -> WeaponModel:
		return WeaponModel.objects.get(name=weapon_name)
