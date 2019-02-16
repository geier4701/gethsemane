from Models.Component import Component


class ShipType(Component):
	def __init__(self, id: int, name: str, mass: int):
		self.id = id
		self.name = name
		self.mass = mass
	
	def get_stat_info(self):
		return {
			'id': self.id,
			'name': self.name,
			'mass': self.mass
		}
