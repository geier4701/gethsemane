import os
import json
from typing import Dict, List
from pathlib import Path
from Components import Radar, Component, JumpDrive
from Components.Computer import Computer
from Components.ImpulseEngine import ImpulseDrive
from ShipType import ShipType
from UI.ValidUserInput import validate_list_input


class ComponentRepository:
	component_library = {
		"ShipType": {"path": "ShipTypes.txt", "component_class": ShipType},
		"Computer": {"path": "Computers.txt", "component_class": Computer},
		"ImpulseEngine": {"path": "ImpulseEngines.txt", "component_class": ImpulseEngine},
		"JumpDrive": {"path": "JumpDrives.txt", "component_class": JumpDrive},
		"Radar": {"path": "Radars.txt", "component_class": Radar}
	}
	
	def get_components_of_type(self, component_type: str) -> List[Component]:
		file = open('TestComponents.json')
		data = json.load(file)
		
		components = []
		if component_type is 'ammunition':
			pass
		if component_type is 'armour':
			pass
		if component_type is 'weapons':
			pass
		if component_type is 'computers':
			for computer in data[component_type]:
				components.append(Computer(data[component_type].index(computer), computer['name'], computer['mass'], computer['repair_cost'], computer['speed'], computer['capacity']))
		if component_type is 'impulse_drives':
			for engine in data[component_type]:
				components.append(ImpulseDrive(data[component_type].index(engine), engine['name'], engine['mass'], engine['repair_cost'], engine['energy_cost'], engine['max_accel']))
		if component_type is 'jump_drives':
			pass
		if component_type is 'radar':
			pass
		if component_type is 'radar':
			pass
		if component_type is 'ship_types':
			pass
		
		file.close()
		
		return components
	
	def old_get_components(self, component_type: str):
		components: Dict[int, Component] = {}
		
		repo_folder = Path(os.path.dirname(__file__))
		file = open(repo_folder / self.component_library[component_type]["path"])
		
		for line in file:
			stats = line.split(",")
			to_add = self.component_library[component_type]["component_class"](*stats)
			components[to_add.component_id] = to_add
		
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
			print("Select your ship's " + component_type)
			for component in components:
				stat_info = components[component].get_stat_info()
				for stat in stat_info:
					print(f"{stat}) - {stat_info[stat]}")
				
			user_choice = input()
			valid = validate_list_input(len(components), user_choice)
		
		return components[user_choice]
