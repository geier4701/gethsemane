from Models import Ship, JumpDrive
from repos import ComponentFetcher
from UI.ValidUserInput import validate_list_input


def get_jump(ship: Ship):
	valid = False
	user_choice: str

	jump_types = ComponentFetcher.get_components(JumpDrive)

	while not valid:
		print("Choose a jump drive")
		for drive in jump_types:
			print(f"{drive.id}) {drive.name} - {drive.mass} tonnes, {drive.cost} teraWatts")
		user_choice = input()
		valid = validate_list_input(jump_types.count(), user_choice)

	ship.computer = jump_types[user_choice]

	return ship
