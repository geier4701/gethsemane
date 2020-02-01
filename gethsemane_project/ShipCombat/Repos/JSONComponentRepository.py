import os
import json
from typing import List
from pathlib import Path
from UI.ValidUserInput import validate_list_input
from gethsemane_project.ShipCombat.Models.Components.Ammunition import Ammunition
from gethsemane_project.ShipCombat.Models.Components.Armour import Armour
from gethsemane_project.ShipCombat.Models.Components.Component import Component
from gethsemane_project.ShipCombat.Models.Components.Computer import Computer
from gethsemane_project.ShipCombat.Models.Components.ImpulseEngine import ImpulseEngine
from gethsemane_project.ShipCombat.Models.Components.JumpDrive import JumpDrive
from gethsemane_project.ShipCombat.Models.Components.Radar import Radar
from gethsemane_project.ShipCombat.Models.Components.Weapon import Weapon
from gethsemane_project.ShipCombat.Repos.ComponentRepository import ComponentRepository


class JSONComponentRepository(ComponentRepository):
	component_library = {
		'ammunitions': Ammunition,
		'armours': Armour,
		'computers': Computer,
		'impulse_engines': ImpulseEngine,
		'jump_drives': JumpDrive,
		'radar': Radar,
		'weapons': Weapon
	}
	
	def get_components_of_type(self, component_type: str) -> List[Component]:
		component_folder = Path(os.path.dirname(__file__))
		file = open(component_folder / 'Repos/TestDatabases/TestComponents.json')
		raw_components = json.load(file)
		
		components = []
		for raw_component in raw_components[component_type]:
			component = self.component_library[component_type](*raw_component)
			components[component.component_id] = component
		
		file.close()
		
		return components
	
	def get_component(self, component_id: int, component_type: str) -> Component:
		components = self.get_components_of_type(component_type)
		return components[component_id]
	
	# TODO: Move this into the UI layer
	def select_component(self, component_type: str):
		valid = False
		user_choice: str
		
		components = self.get_components_of_type(component_type)
		
		while not valid:
			os.system('cls')
			print("Select your ship's " + component_type)
			for component in components:
				stat_info = components[component].get_stat_info()
				for stat in stat_info:
					print(f"{stat}) - {stat_info[stat]}")
				
			user_choice = input()
			valid = validate_list_input(len(components), user_choice)
		
		return components[user_choice]