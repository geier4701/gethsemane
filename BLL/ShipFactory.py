from Ship import Ship
from repos.ComponentRepository import ComponentRepository


class ShipFactory:
	def create_ship(self):
		created_ship = Ship()
		self.update_ship(created_ship)
	
	def update_ship(self, created_ship: Ship):
		type_fetcher = ComponentRepository()
		
		selected_component = type_fetcher.select_component("ShipType")
		created_ship.ship_class = selected_component
		
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
