class ShipType:
	ship_type_id: int
	name: str
	weight: int
	power_gen: int
	battery_max: int
	
	def __init__(self, ship_type_id: int, name: str, weight: int, power_gen: int, battery_max: int):
		self.ship_type_id = ship_type_id
		self.name = name
		self.weight = weight
		self.power_gen = power_gen
		self.battery_max = battery_max
	
	def get_stat_info(self):
		return {
			'id': self.ship_type_id,
			'name': self.name,
			'weight': self.weight
		}
