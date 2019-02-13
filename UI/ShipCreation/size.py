import os

import Ship
from ShipType import ShipType
from repos import ComponentFetcher
from UI.ValidUserInput import validate_list_input


def get_type(component: Ship, component_type: str):
	valid = False
	user_choice: str
	
	components = ComponentFetcher.get_components(component_type)
	
	while not valid:
		os.system('cls')
		print("Select your " + component_type)
		
		for component in components:
			print(f"{component.id}) {component.name} - {component.mass} tonnes")
			
		user_choice = input()
		valid = validate_list_input(components.count(), user_choice)
	
	component.s_class = components[user_choice]
	
	return component
