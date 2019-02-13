from Models.Component import Component


class JumpDrive(Component):
	jump_cost: int
	
	def __init__(self, id: int, name: str, mass: int, jump_cost: int):
		self.id = id
		self.name = name
		self.mass = mass
		self.jump_cost = jump_cost
	
	def get_stat_info(self):
		pass
