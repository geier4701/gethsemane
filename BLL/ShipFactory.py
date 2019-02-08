from Ship import Ship
from UI.ShipCreation.size import get_type


class ShipFactory:
	def create_ship(self):
		# PASS THE SHIP AROUND AS THINGS ARE ADDED
		ship = Ship()
		
		ship = get_type(ship)
		
		print("Choose a jump drive")
		print("1) SP500 - it works")
		jump = input()
		
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
