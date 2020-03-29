from api.ShipCombat.Models.Coordinates import Coordinates


class ActionRecord:
	success: bool
	ship_location: Coordinates
	component_states: list
	health: int
	action_name: str
	target: Coordinates
	
	def __init__(
			self,
			success: bool,
			ship_location: Coordinates,
			component_states: list,
			health: int,
			action_name: str,
			target: Coordinates = None
	):
		self.success = success
		self.ship_location = ship_location
		self.component_states = component_states
		self.health = health
		self.action_name = action_name
		self.target = target
