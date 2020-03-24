from api.ShipCombat.Models.Subroutines.Actions.Action import Action


class AttemptRepairs(Action):
	name = "AR"
	target_component_name: str
	
	def __init__(self, action_id: int, target_component_name: str):
		self.action_id = action_id
		self.target_component_name = target_component_name
