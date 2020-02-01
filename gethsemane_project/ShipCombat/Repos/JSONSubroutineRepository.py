import os
from pathlib import Path
import json
from typing import List
from gethsemane_project.ShipCombat.Models.Subroutines.Actions.AttemptRepairs import AttemptRepairs
from gethsemane_project.ShipCombat.Models.Subroutines.Actions.Delay import Delay
from gethsemane_project.ShipCombat.Models.Subroutines.Actions.FireImpulse import FireImpulse
from gethsemane_project.ShipCombat.Models.Subroutines.Actions.FireWeapon import FireWeapon
from gethsemane_project.ShipCombat.Models.Subroutines.Actions.Jump import Jump
from gethsemane_project.ShipCombat.Models.Subroutines.Actions.Scan import Scan
from gethsemane_project.ShipCombat.Models.Subroutines.Conditions.AmmunitionLevel import AmmunitionLevel
from gethsemane_project.ShipCombat.Models.Subroutines.Conditions.Condition import Condition
from gethsemane_project.ShipCombat.Models.Subroutines.Conditions.Distance import Distance
from gethsemane_project.ShipCombat.Models.Subroutines.Conditions.EnergyLevel import EnergyLevel
from gethsemane_project.ShipCombat.Models.Subroutines.Conditions.Health import Health
from gethsemane_project.ShipCombat.Models.Subroutines.Conditions.IsDisabled import IsDisabled
from gethsemane_project.ShipCombat.Models.Subroutines.Subroutine import Subroutine
from gethsemane_project.ShipCombat.Repos.SubroutineRepository import SubroutineRepository


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
