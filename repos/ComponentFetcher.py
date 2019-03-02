import os
from typing import Dict
from pathlib import Path

import ImpulseEngine
from Models import Component, Computer, JumpDrive, Radar
from ShipType import ShipType
from UI.ValidUserInput import validate_list_input


# THIS WHOLE FILE IS UNNECESSARY, AVAILABLE COMPONENTS CAN BE CODED INTO IN-MEMORY REPO
# DELETE IN THE FUTURE
class ComponentFetcher:
	component_library = {
		"ShipType": {"path": "ShipTypes.txt", "component_class": ShipType},
		"Computer": {"path": "Computers.txt", "component_class": Computer},
		"ImpulseEngine": {"path": "ImpulseEngines.txt", "component_class": ImpulseEngine},
		"JumpDrive": {"path": "JumpDrives.txt", "component_class": JumpDrive},
		"Radar": {"path": "Radars.txt", "component_class": Radar}
	}
	
	def get_components(self, component_type: str):
		components: Dict[int, Component] = {}
		
		repo_folder = Path(os.path.dirname(__file__))
		file = open(repo_folder / self.component_library[component_type]["path"])
		
		for line in file:
			stats = line.split(",")
			to_add = self.component_library[component_type]["component_class"](*stats)
			components[to_add.id] = to_add
		
		file.close()
		
		return components
	
	def get_component(self, id: int, component_type: str):
		components = self.get_components(component_type)
		
		return components[id]
	
	def select_component(self, component_type: str):
		valid = False
		user_choice: str
		
		components = self.get_components(component_type)
		
		while not valid:
			os.system('cls')
			print("Select your ship's" + component_type)
			for component in components:
				stat_info = components[component].get_stat_info()
				for stat in stat_info:
					print(f"{stat}) - {stat_info[stat]}")
				
			user_choice = input()
			valid = validate_list_input(len(components), user_choice)
		
		return components[user_choice]
