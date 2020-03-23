from api.ShipCombat.Models.Subroutines.Actions.Action import Action


class Jump(Action):
	name = "Jump"
	distance_from_enemy: int
	
	def __init__(self, action_id: int, distance_from_enemy: int):
		self.action_id = action_id
		self.distance_from_enemy = distance_from_enemy
