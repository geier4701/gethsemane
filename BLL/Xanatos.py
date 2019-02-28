from BLL.Horatio import Horatio
from Models.Ship import Ship
from Subroutines.Actions import FireWeapon


class Xanatos:
	player_ship: Ship
	opponent_ship: Ship
	
	def __init__(self, player: Ship, opponent: Ship):
		self.player_ship = player
		self.opponent_ship = opponent
	
	def gambit(self):
		player_captain = Horatio(self.player_ship)
		opponent_captain = Horatio(self.opponent_ship)

		while self.player_ship.health > 0 and self.opponent_ship.health > 0:
			player_to_perform = player_captain.command()
			opponent_to_perform = opponent_captain.command()
			
			# BREAK THIS OUT INTO REUSABLE CODE
			for action in player_to_perform:
				if action is FireWeapon:
					action.activate(self.player_ship.radar.enemy_coord)
