from datetime import datetime
from typing import List

from api.ShipCombat.Models.ActionRecord import ActionRecord
from api.ShipCombat.Models.Coordinates import Coordinates
from api.ShipCombat.Models.Ship import Ship
from api.ShipCombat.Models.Subroutines.Actions.Action import Action
from api.ShipCombat.Models.Subroutines.Subroutine import Subroutine


class BattleRecorder:
	battle_record: List[ActionRecord]
	subroutine_record: List[str]
	test_record: List[str]
	
	def __init__(self):
		self.battle_record = []
		self.subroutine_record = []
		self.test_record = []
	
	def record_subroutines(self, subroutines: List[Subroutine]):
		for subroutine in subroutines:
			actions = '\nActions: '
			for action in subroutine.actions:
				actions = actions + action.name + ' '
			conditions = '\nConditions: '
			for condition in subroutine.conditions:
				conditions = conditions + '\nCondition name: ' + condition.name + '\nAt least: ' + str(condition.at_least) + '\nAt most: ' + str(condition.at_most)
				
			self.subroutine_record.append(
				'\nship id:' + str(subroutine.ship_id) +
				'\nsubroutine id: ' + str(subroutine.subroutine_id) +
				'\npriority: ' + str(subroutine.priority) +
				actions + conditions
			)
	
	def record_test(self, result: str):
		self.test_record.append(result)
	
	def record_action(self, success: bool, ship: Ship, action: Action, target: Coordinates = None) -> None:
		component_states = [
			ship.name,
			"Health: " + str(ship.ship_class.health),
			"Energy: " + str(ship.current_energy)
		]

		self.battle_record.append(ActionRecord(success, ship.coordinates, component_states, ship.ship_class.health, action.name, target))
	
	# TODO: This needs to refactored to something savable/consumable on the front end
	def export_battle(self, victor: str) -> None:
		now = datetime.now()
		f = open("battle_" + str(datetime.timestamp(now)), "w+")
		
		for record in self.battle_record:
			f.write("Current ship state:\n")
			for ship_state in record.component_states:
				f.write("\nship_state: " + ship_state)
				
			f.write(
				"\nShip is at location: \nx: %s\n y: %s\n z: %s\nTravelling at a speed of: \nx: %s\n y: %s\n z: %s\n" %
				(record.ship_location.location[0], record.ship_location.location[1], record.ship_location.location[2],
					record.ship_location.speed[0], record.ship_location.speed[1], record.ship_location.speed[2])
			)
			f.write("Ship attempted the following action: " + record.action_name + "\n")
			
			if record.success:
				f.write("It succeeded spectacularly!\n")
			else:
				f.write("It failed miserably...\n")
			
			if record.target is not None:
				f.write(
					"Weapon fired at: \nx: %s\n y: %s\n z: %s\nWith an assumed enemy speed of: \nx: %s\n y: %s\n z: %s\n" %
					(record.target.location[0], record.target.location[1], record.target.location[2],
						record.target.speed[0], record.target.speed[1], record.target.speed[2])
				)
			
			f.write("\n\n")
		
		for record in self.subroutine_record:
			f.write(record)
		
		for result in self.test_record:
			f.write('\nTest result: ' + result)
		
		f.write("And the winner is: " + victor + "!")
		f.close()
