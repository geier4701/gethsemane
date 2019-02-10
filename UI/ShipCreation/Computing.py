from Models import Ship, Computer
from repos import ComponentFetcher
from UI.ValidUserInput import validate_list_input


def get_comp(ship: Ship):
	valid = False
	user_choice: str

	computer_types = ComponentFetcher.get_components(Computer)

	while not valid:
		print("Choose a computer")
		for computer in computer_types:
			print(f"{computer.id}) {computer.name} - {computer.mass} tonnes, {computer.speed}gHz, {computer.capacity} terabytes")
		user_choice = input()
		valid = validate_list_input(computer_types.count(), user_choice)

	ship.computer = computer_types[user_choice]

	return ship
