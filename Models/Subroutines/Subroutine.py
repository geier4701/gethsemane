class Subroutine:
	priority: int
	conditions: []
	actions: []
	
	def __init__(self, priority, conditions, actions):
		self.priority = priority
		self.conditions = conditions
		self.actions = actions
