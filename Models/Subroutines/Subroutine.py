class Subroutine:
	id: int
	name: str
	ship_id: int
	priority: int
	conditions: []
	actions: []
	
	def __init__(self, id, name, ship_id, priority, conditions, actions):
		self.name = name
		self.id = id
		self.ship_id = ship_id
		self.priority = priority
		self.conditions = conditions
		self.actions = actions
