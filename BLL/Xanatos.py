from BLL.Horatio import Horatio
from Models.Ship import Ship


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

		# SHOULD ACTIONS OR MOVEMENT HAPPEN FIRST?
		while self.player_ship.health > 0 and self.npc_ship.health > 0:
			player_captain.command()
			opponent_captain.command()
			self.move_ship(self.player_ship)
			self.move_ship(self.npc_ship)
