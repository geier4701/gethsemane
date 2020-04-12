from api.ShipCombat.Repos.ShipTypeRepository import ShipTypeRepository


class ShipTypeManager:
	ship_type_repo: ShipTypeRepository
	
	def __init__(self, ship_type_repo: ShipTypeRepository):
		self.ship_type_repo = ship_type_repo
	
	def get_available_ship_types(self, character_id: int):
		return self.ship_type_repo.find_by_character_id(character_id)
