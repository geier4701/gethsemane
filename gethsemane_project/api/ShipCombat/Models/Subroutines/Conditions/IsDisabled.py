from ...Ship import Ship
from .Condition import Condition


class IsDisabled(Condition):
	component_id: int
	
	def __init__(self, at_least: int, at_most: int, component_id: int):
		self.at_least = at_least
		self.at_most = at_most
		self.component_id = component_id
		
	def test(self, own_ship: Ship, enemy_ship: Ship):
		component = own_ship.get_components()[self.component_id]
		return component.operational
