from api.ShipCombat.Models.Subroutines.Actions.Action import Action


class Scan(Action):
	name = "Scan"
	
	def __init__(self, action_id: int):
		self.action_id = action_id
