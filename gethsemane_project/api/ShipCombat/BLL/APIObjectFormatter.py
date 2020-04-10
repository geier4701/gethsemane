from typing import List, Dict

from api.ShipCombat.Models.Components.Component import Component
from api.ShipCombat.Models.Ship import Ship
from api.ShipCombat.Models.ShipType import ShipType


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
	
	@staticmethod
	def format_ship_class(ship_class: ShipType) -> []:
		pass
	
	@staticmethod
	def format_ship_classes(ship_classes: List[ShipType]) -> []:
		pass
