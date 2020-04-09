from api.models import ShipTypeModel


class ShipType:
	ship_type_id: int
	name: str
	weight: int
	power_gen: int
	battery_max: int
	health: int
	
	def __init__(self, ship_type_model: ShipTypeModel):
		self.ship_type_id = ship_type_model.ship_type_id
		self.name = ship_type_model.name
		self.weight = ship_type_model.weight
		self.power_gen = ship_type_model.power_gen
		self.battery_max = ship_type_model.battery_max
		self.health = ship_type_model.health
