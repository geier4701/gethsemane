class Subroutine:
	ship_id: int
	priority: int
	conditions: []
	actions: []
	
	def __init__(self, ship_id, priority, conditions, actions):
		self.ship_id = ship_id
		self.priority = priority
		self.conditions = conditions
		self.actions = actions
