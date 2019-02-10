from Models.Component import Component


class ImpulseDrive(Component):
	max_accel: int
	
	def __init__(self, id: int, name: str, mass: int, max_accel: int):
		self.id = id
		self.name = name
		self.mass = mass
		self.max_accel = max_accel
