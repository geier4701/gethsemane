from Ship import Ship
from repos.ComponentFetcher import ComponentFetcher


class ShipFactory:
	def create_ship(self):
		created_ship = Ship()
		
		type_fetcher = ComponentFetcher("ShipType")
		selected_component = type_fetcher.select_component()
		created_ship.size = selected_component
		
		print("Choose an impulse engine")
		print("1) Cavalier - zoom!")
		impulse = input()
		
		print("Choose a cpu")
		print("1) MAKE CPU")
		cpu = input()
		
		print("Choose a sensor array")
		print("1) MAKE ACTIVE SCANNER")
		active = input()
		
		print("Choose a passive scanner")
		print("1) MAKE A PASSIVE SCANNER")
		passive = input()
		
		# SAVE SHIP