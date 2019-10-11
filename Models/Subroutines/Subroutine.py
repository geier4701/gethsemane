class Subroutine:
	subroutine_id: int
	name: str
	ship_id: int
	priority: int
	conditions: list
	actions: list
	
	# WHAT IS ALL THIS, DO I NEED ALL THIS?
	def __init__(self, subroutine_id, name, ship_id, priority, conditions, actions):
		self.name = name
		self.subroutine_id = subroutine_id
		self.ship_id = ship_id
		self.priority = priority
		self.conditions = conditions
		self.actions = actions
