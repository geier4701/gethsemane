from gethsemane_project.ShipCombat.BLL.Horatio import Horatio
from gethsemane_project.ShipCombat.Models.Subroutines.Actions.Action import Action


class Delay(Action):
	
	def activate(self, captain: Horatio, info=None):
		return True
