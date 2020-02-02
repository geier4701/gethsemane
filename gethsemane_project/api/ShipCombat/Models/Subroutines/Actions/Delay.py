from ....BLL.Horatio import Horatio
from .Action import Action


class Delay(Action):
	
	def activate(self, captain: Horatio, info=None):
		return True
