import Ship
from ShipTypes import Frigate
from UI.ValidUserInput import validate_list_input


def get_type(ship: Ship):
	valid = False
	s_class: str
	
	while not valid:
		print("Choose a ship size")
		print("1) Frigate")
		s_class = input()
		valid = validate_list_input(1, s_class)
	
	if s_class == "1":
		ship.s_class = Frigate
	
	return ship
