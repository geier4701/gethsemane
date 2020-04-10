from api.ShipCombat.Repos.ShipTypeRepository import ShipTypeRepository


class ShipClassManager:
	ship_type_repo: ShipTypeRepository
	
	def __init__(self, ship_type_repo: ShipTypeRepository):
		self.ship_type_repo = ship_type_repo
	
	def get_available_ship_classes(self, character_id: int):
		return self.ship_type_repo.find_by_character_id(character_id)
