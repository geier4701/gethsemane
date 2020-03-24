from api.ShipCombat.Models.Subroutines.Actions.Action import Action


class Delay(Action):
	name = "DE"
	
	def __init__(self, action_id: int):
		self.action_id = action_id
