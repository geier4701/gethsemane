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
					conditions.append(condition_type(*raw_condition['args']))
				
				raw_actions = raw_subroutine['actions']
				actions = []
				for raw_action in raw_actions:
					action_type = self.action_library[raw_action['name']]
					action_type: Action
					actions.append(action_type(*raw_action['args']))
				
				subroutine = Subroutine(raw_subroutine['subroutine_id'], raw_subroutine['ship_id'], raw_subroutine['priority'], conditions, actions)
				subroutines.append(subroutine)
		
		file.close()
		return subroutines
	
	def get_subroutine(self, subroutine_id: int) -> Subroutine:
		pass
