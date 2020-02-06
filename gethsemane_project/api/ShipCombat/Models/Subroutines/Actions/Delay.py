from api.ShipCombat.BLL.Horatio import Horatio
from api.ShipCombat.Models.Subroutines.Actions.Action import Action


class Delay(Action):
	name = "Delay"
	
	def __init__(self, action_id: int):
		self.action_id = action_id
	
	def activate(self, captain: Horatio, info=None):
		return True
