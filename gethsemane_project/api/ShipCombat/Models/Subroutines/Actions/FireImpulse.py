from api.ShipCombat.Models.Coordinates import Coordinates
from api.ShipCombat.Models.Subroutines.Actions.Action import Action


class FireImpulse(Action):
	name = "FireImpulse"
	velocity_change: Coordinates
	
	def __init__(self, action_id: int, velocity_change: Coordinates):
		self.action_id = action_id
		self.velocity_change = velocity_change
