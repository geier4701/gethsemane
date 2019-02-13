from Ship import Ship
from repos.ComponentFetcher import ComponentFetcher


class ShipFactory:
	def create_ship(self):
		# PASS THE SHIP AROUND AS THINGS ARE ADDED
		fetcher = ComponentFetcher()
		created_ship = Ship()
		
		selected_component = fetcher.select_component("ShipType")
		created_ship[selected_component.name] = selected_component
		
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
