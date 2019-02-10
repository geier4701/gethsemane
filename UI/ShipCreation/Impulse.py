from Models import Ship, ImpulseEngine
from repos import ComponentFetcher
from UI.ValidUserInput import validate_list_input


def get_impulse(ship: Ship):
	valid = False
	user_choice: str

	impulse_types = ComponentFetcher.get_components(ImpulseEngine)

	while not valid:
		print("Choose an impulse engine")
		for engine in impulse_types:
			print(f"{engine.id}) {engine.name} - {engine.mass} tonnes, {engine.mass_accel} newtons")
		user_choice = input()
		valid = validate_list_input(impulse_types.count(), user_choice)

	ship.s_class = impulse_types[user_choice]

	return ship
