from Component import Component


class ShipType(Component):
	def __init__(self, id: int, name: str, mass: int):
		self.id = id
		self.name = name
		self.mass = mass
