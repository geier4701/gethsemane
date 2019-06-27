from BLL.Horatio import Horatio
from Models.Ship import Ship
from Subroutines.Actions import FireWeapon, FireImpulse, Jump, Scan, AttemptRepairs


class Xanatos:
	player_ship: Ship
	npc_ship: Ship
	
	def __init__(self, player: Ship, opponent: Ship):
		self.player_ship = player
		self.npc_ship = opponent
	
	def move_ship(self, ship: Ship):
		ship.location.location[0] += ship.location.speed[0]
		ship.location.location[1] += ship.location.speed[1]
		ship.location.location[2] += ship.location.speed[2]
	
	def gambit(self):
		player_captain = Horatio(self.player_ship)
		opponent_captain = Horatio(self.npc_ship)

		while self.player_ship.health > 0 and self.npc_ship.health > 0:
			self.move_ship(self.player_ship)
			self.move_ship(self.npc_ship)
			self.engage(player_captain.command(), player_captain, opponent_captain)
			self.engage(opponent_captain.command(), player_captain, opponent_captain)
	
	def engage(self, actions, captain: Horatio, enemy_captain: Horatio):
		for action in actions:
			if action is FireImpulse:
				action.activate(captain)
			if action is FireWeapon:
				# THIS IS GOING TO NEED TO SOMEHOW TALK WITH XANATOS TO ACTUALLY TAKE ACTION ON ENEMY SHIP
				action.activate(captain)
			if action is Jump:
				# THIS NEEDS TO SOMEHOW KNOW WHAT THE DESIRED COORDINATES ARE
				action.activate(captain)
			if action is Scan:
				if action.activate(captain):
					captain.enemy_intel.current_energy = enemy_captain.own_ship.current_energy
					captain.enemy_intel.location = enemy_captain.own_ship.location
					captain.enemy_intel.direction = enemy_captain.own_ship.direction
					captain.enemy_intel.health = enemy_captain.own_ship.health
			if action is AttemptRepairs:
				# THIS NEEDS TO KNOW WHICH COMPONENT TO REPAIR
				pass
