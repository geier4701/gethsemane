import os
from typing import Dict
from pathlib import Path

import ImpulseEngine
from Models import Component, Computer, JumpDrive, Radar
from ShipType import ShipType
from UI.ValidUserInput import validate_list_input


class ComponentFetcher:
	# IF THIS IS INSERTED AT INSTANTIATION BY A MANAGER/FACTORY WE CAN TEST IT
	component_library = {
		"ShipType": {"path": "ShipTypes.txt", "component_class": ShipType},
		"Computer": {"path": "Computers.txt", "component_class": Computer},
		"ImpulseEngine": {"path": "ImpulseEngines.txt", "component_class": ImpulseEngine},
		"JumpDrive": {"path": "JumpDrives.txt", "component_class": JumpDrive},
		"Radar": {"path": "Radars.txt", "component_class": Radar}
	}
	component_type: str
	
	def __init__(self, component_type: str):
		self.component_type = component_type
	
	def get_components(self):
		components: Dict[int, Component] = {}
		
		repo_folder = Path(os.path.dirname(__file__))
		# contents = repo_folder / self.component_library[self.component_type]["path"]
		fhand = open(repo_folder / self.component_library[self.component_type]["path"])
		
		for line in fhand:
			stats = line.split(",")
			to_add = self.component_library[self.component_type]["component_class"](*stats)
			components[to_add.id] = to_add
		
		return components
	
	def get_component(self, id: int):
		components = self.get_components()
		
		return components[id]
	
	def select_component(self):
		valid = False
		user_choice: str
		
		components = self.get_components()
		
		while not valid:
			os.system('cls')
			print("Select your " + self.component_type)
			
			for component in components:
				stat_info = components[component].get_stat_info()
				for stat in stat_info:
					print(f"{stat['name']}) - {stat['value']}")
				
			user_choice = input()
			valid = validate_list_input(len(components), user_choice)
		
		return components[user_choice]
