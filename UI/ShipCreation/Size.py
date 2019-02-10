from Models import Ship, ShipType
from repos import ComponentFetcher
from UI.ValidUserInput import validate_list_input


def get_type(ship: Ship):
	valid = False
	user_choice: str
	
	ship_types = ComponentFetcher.get_components(ShipType)
	
	while not valid:
		print("Choose a ship size")
		for ship in ship_types:
			print(f"{ship.id}) {ship.name} - {ship.mass} tonnes")
		user_choice = input()
		valid = validate_list_input(ship_types.count(), user_choice)
	
	ship.s_class = ship_types[user_choice]
	
	return ship
