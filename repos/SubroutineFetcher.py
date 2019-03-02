import os
from pathlib import Path
import json

from Subroutines.Actions import AttemptRepairs, FireImpulse, FireWeapon, Jump, Scan, Action
from Subroutines.States import Health, EnergyLevel, Distance, AmmunitionLevel, Condition
from Subroutines.Subroutine import Subroutine


# BASE SHIP LOADER ON THIS CLASS
class SubroutineFetcher:
	subroutine_library = {
		"Health": Health,
		"EnergyLevel": EnergyLevel,
		"Distance": Distance,
		"AmmunitionLevel": AmmunitionLevel,
		"AttemptRepairs": AttemptRepairs,
		"FireImpulse": FireImpulse,
		"FireWeapon": FireWeapon,
		"Jump": Jump,
		"Scan": Scan
	}
	
	def get_subroutines(self, controlling_ship_id: int):
		subroutines = []
		
		subroutine_folder = Path(os.path.dirname(__file__))
		with open(subroutine_folder / 'Subroutines.json') as file:
			sub_rout_blob = json.load(file)
		
		for blob in sub_rout_blob:
			if blob['ship_id'] == controlling_ship_id:
				conblob = blob['conditions']
				conditions = []
				for con in conblob:
					con_type = self.subroutine_library[con['name']]
					con_type: Condition
					conditions.append(con_type(conblob['args']))
				
				act_blob = blob['actions']
				actions = []
				for act in act_blob:
					act_type = self.subroutine_library[act['name']]
					act_type: Action
					actions.append(act_type(act_blob['args']))
				
				subroutine = Subroutine(blob['id'], blob['name'], blob['ship_id'], blob['priority'], conditions, actions)
				subroutines.append(subroutine)
		
		file.close()
		return subroutines
