from typing import List, Dict

from api.ShipCombat.Models.Components.Component import Component
from api.ShipCombat.Models.Ship import Ship


# TODO: All of this! Then set up the front end to consume
class APIObjectFormatter:
	@staticmethod
	def format_ship(ship: Ship) -> []:
		pass
	
	@staticmethod
	def format_ships(ships: List[Ship]) -> []:
		pass
	
	@staticmethod
	def format_component(component: Component) -> []:
		pass
	
	@staticmethod
	def format_components(components: Dict[str, List[Component]]) -> []:
		pass
