import os
from typing import Dict

import ImpulseEngine
from Component import Component
from Computer import Computer
from JumpDrive import JumpDrive
from Radar import Radar
from Ship import Ship
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
	
	def get_components(self, component_type: str):
		components: Dict[int, Component] = {}
		
		fhand = open(self.component_library[component_type]["path"])
		
		for line in fhand:
			stats = line.split(",")
			to_add = self.component_library[component_type]["component_class"](*stats)
			components[to_add.id] = to_add
		
		return components
	
	def get_component(self, component_type: str, id: int):
		components = self.get_components(component_type)
		
		return components[id]
	
	def select_component(self, component_type: str):
		valid = False
		user_choice: str
		
		components = self.get_components(component_type)
		
		while not valid:
			os.system('cls')
			print("Select your " + component_type)
			
			component: Component
			for component in components:
				stat_info = component.get_stat_info()
				for stat in stat_info:
					print(f"{stat['name']}) - {stat['value']}")
				
			user_choice = input()
			valid = validate_list_input(len(components), user_choice)
		
		return components[user_choice]
