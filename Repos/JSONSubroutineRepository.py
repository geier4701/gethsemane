import os
from pathlib import Path
import json
from typing import List
from Subroutines.Actions import AttemptRepairs, FireImpulse, FireWeapon, Jump, Scan, Action, Delay
from Subroutines.Conditions import Health, EnergyLevel, Distance, AmmunitionLevel, Condition, IsDisabled
from Subroutines.Subroutine import Subroutine
from Repos.SubroutineRepository import SubroutineRepository


class JSONSubroutineRepository(SubroutineRepository):
	condition_library = {
		"health": Health,
		"energy_level": EnergyLevel,
		"distance": Distance,
		"ammunition_level": AmmunitionLevel,
		"is_disabled": IsDisabled
	}
	
	action_library = {
		"attempt_repairs": AttemptRepairs,
		"fire_impulse": FireImpulse,
		"fire_weapon": FireWeapon,
		"jump": Jump,
		"scan": Scan,
		"delay": Delay
	}
	
	# TODO: Write a subroutine Test Database and update this function
	def get_subroutines(self, controlling_ship_id: int) -> List[Subroutine]:
		subroutines = []
		
		subroutine_folder = Path(os.path.dirname(__file__))
		file = open(subroutine_folder / 'Repos/TestDatabases/TestSubroutines.json')
		raw_subroutines = json.load(file)
		
		for raw_subroutine in raw_subroutines:
			if raw_subroutine['ship_id'] == controlling_ship_id:
				raw_conditions = raw_subroutine['conditions']
				conditions = []
				for raw_condition in raw_conditions:
					condition_type = self.condition_library[raw_condition['name']]
					condition_type: Condition
					conditions.append(condition_type(raw_conditions['args']))
				
				raw_actions = raw_subroutine['actions']
				actions = []
				for raw_action in raw_actions:
					act_type = self.action_library[raw_action['name']]
					act_type: Action
					actions.append(act_type(raw_actions['args']))
				
				subroutine = Subroutine(raw_subroutine['subroutine_id'], raw_subroutine['name'], raw_subroutine['ship_id'], raw_subroutine['priority'], conditions, actions)
				subroutines.append(subroutine)
		
		file.close()
		return subroutines
	
	def get_subroutine(self, subroutine_id: int) -> Subroutine:
		pass
