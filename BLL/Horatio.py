from Ship import Ship
from Subroutines.Actions import FireWeapon, FireImpulse, Jump, Scan, AttemptRepairs


class Horatio:
	subroutines: []
	own_ship: Ship
	last_action: []
	enemy_ship: Ship
	
	def __init__(self, ship):
		self.own_ship = ship
		self.subroutines = ship.subroutines
		self.enemy_ship = Ship()
	
	def command(self):
		self.subroutines.sort(self, self.subroutines.priority)
		actions_to_take = []
		for subroutine in self.subroutines:
			make_it_so = True
			for condition in subroutine.conditions:
				if not condition.test(self.own_ship, self.enemy_ship):
					make_it_so = False
			
			if make_it_so:
				self.last_action = subroutine.actions
				actions_to_take = subroutine.actions
		
		if not actions_to_take:
			actions_to_take = self.last_action
		
		self.engage(actions_to_take)
	
	def engage(self, actions):
		for action in actions:
			if action is FireImpulse:
				# THIS NEEDS TO SOMEHOW KNOW WHAT THE VELOCITY CHANGE DESIRED IS
				action.activate(self.own_ship, velocity_change)
			if action is FireWeapon:
				# THIS IS GOING TO NEED TO SOMEHOW TALK WITH XANATOS TO ACTUALLY TAKE ACTION ON ENEMY SHIP
				action.activate(self.enemy_ship.location)
			if action is Jump:
				# THIS NEEDS TO SOMEHOW KNOW WHAT THE DESIRED COORDINATES ARE
				action.activate(self.own_ship, new_location)
			if action is Scan:
				# THIS NEEDS TO ACCESS THE ENEMY SHIP'S TRUE STATE
				action.activate(self.own_ship, self.enemy_ship)
			if action is AttemptRepairs:
				# THIS NEEDS TO KNOW WHICH COMPONENT TO REPAIR
				pass
