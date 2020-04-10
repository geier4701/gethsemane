from typing import List

from api.models import ShipModel, WeaponModel, AmmunitionModel


class ShipRepository:
	def find_by_id(self, ship_id: int) -> ShipModel:
		return ShipModel.objects.get(ship_id=ship_id)
	
	def find_by_character_id(self, character_id: int) -> List[ShipModel]:
		return ShipModel.objects.filter(character_id=character_id)
	
	def save_ship(
			self,
			ship_model: ShipModel,
			weapons: List[WeaponModel],
			ammunitions: [AmmunitionModel]
	) -> int:
		ship_model.clean_fields(exclude='ship_id')
		if ship_model.ship_id is not None:
			ship_model.weapon_set.clear()
			ship_model.ammunition_set.clear()
		
		ship_model.save()
		
		for weapon in weapons:
			ship_model.weapons.add(weapon)
		for ammo in ammunitions:
			ship_model.ammunitions.add(ammo)
		
		return ship_model.ship_id
	
	def find_by_character_and_name(self, user_name: str, ship_name: str):
		# THIS WILL TAKE OVER FIND_BY_NAME TO ALLOW FOR NON-UNIQUE NAMES
		pass
