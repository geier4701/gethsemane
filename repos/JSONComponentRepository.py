import os
import json
from typing import Dict
from Components import Component
from Components.Ammunition import Ammunition, AmmunitionType, DamageType
from Components.Armour import Armour, ArmourType
from Components.Computer import Computer
from Components.ImpulseEngine import ImpulseEngine
from Components.JumpDrive import JumpDrive
from Components.Radar import Radar
from Components.Weapon import Weapon
from ShipType import ShipType
from UI.ValidUserInput import validate_list_input
from repos.ComponentRepository import ComponentRepository


class JSONComponentRepository(ComponentRepository):
	def get_components_of_type(self, component_type: str) -> Dict[int, Component]:
		file = open('TestComponents.json')
		data = json.load(file)
		
		components = {}
		if component_type is 'ammunition':
			for munition in data['armament'][component_type]:
				components[data[component_type].index(munition)] = \
					Ammunition(data[component_type].index(munition), munition['name'], munition['mass'], 0, DamageType(munition['damage_type']), AmmunitionType(munition['ammunition_type']), munition['max_ammo'])
		if component_type is 'armours':
			for armour in data['armament'][component_type]:
				components[data[component_type].index(armour)] = \
					Armour(data[component_type].index(armour), armour['name'], armour['mass'], armour['repair_cost'], ArmourType(armour['armour_type']))
		if component_type is 'weapons':
			for weapon in data['armament'][component_type]:
				components[data[component_type].index(weapon)] = \
					Weapon(data[component_type].index(weapon), weapon['name'], weapon['mass'], weapon['repair_cost'], weapon['damage'], AmmunitionType(weapon['ammunition_type']), weapon['munition_velocity'], weapon['energy_cost'])
		if component_type is 'computers':
			for computer in data[component_type]:
				components[data[component_type].index(computer)] = \
					Computer(data[component_type].index(computer), computer['name'], computer['mass'], computer['repair_cost'], computer['speed'], computer['capacity'])
		if component_type is 'impulse_engine':
			for engine in data[component_type]:
				components[data[component_type].index(engine)] = \
					ImpulseEngine(data[component_type].index(engine), engine['name'], engine['mass'], engine['repair_cost'], engine['energy_cost'], engine['max_accel'])
		if component_type is 'jump_drives':
			for drive in data[component_type]:
				components[data[component_type].index(drive)] = \
					JumpDrive(data[component_type].index(drive), drive['name'], drive['mass'], drive['repair_cost'], drive['jump_cost'])
		if component_type is 'radars':
			for radar in data[component_type]:
				components[data[component_type].index(radar)] = \
					Radar(data[component_type].index(radar), radar['name'], radar['mass'], radar['repair_cost'], radar['tracking_style'], radar['energy_cost'])
		if component_type is 'ship_types':
			for ship_type in data[component_type]:
				components[data[component_type].index(ship_type)] = \
					ShipType(data[component_type].index(ship_type), ship_type['name'], ship_type['weight'], ship_type['power_gen'], ship_type['battery_max'])
		
		file.close()
		
		return components
	
	def get_component(self, component_id: int, component_type: str):
		components = self.get_components_of_type(component_type)
		return components[component_id]
	
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
