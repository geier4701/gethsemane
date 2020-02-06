from typing import List

from api.ShipCombat.BLL.Horatio import Horatio
from api.ShipCombat.Models import Ship
from api.ShipCombat.Models.Components.Weapon import Weapon
from api.ShipCombat.Models.Subroutines.Actions import FireWeapon, Scan


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
			self.generate_energy([self.player_ship, self.opponent_ship])
			self.move_ships([self.player_ship, self.opponent_ship])
			self.engage(player_captain.command(), player_captain, opponent_captain)
			self.engage(opponent_captain.command(), opponent_captain, player_captain)
	
	def engage(self, actions, captain: Horatio, enemy_captain: Horatio, info=None):
		for action in actions:
			action_result = action.activate(captain, info)
			if action is FireWeapon:
				if action_result.coord == enemy_captain.own_ship.location and action_result.ammo is not None:
					# TODO: Track weapons / Check enemy ship speed as well as location
					# TODO: Implement armour
					self.deal_damage(enemy_captain.own_ship, action_result.weapon)
			if action is Scan and action_result is True:
				captain.enemy_intel = enemy_captain.own_ship
	
	def move_ships(self, ships: List[Ship]):
		for ship in ships:
			loc = 0
			while loc < 3:
				ship.location.location[loc] += ship.location.speed[loc]
				loc += 1
	
	def generate_energy(self, ships: List[Ship]):
		for ship in ships:
			energy = ship.current_energy + ship.ship_class.power_gen
			if energy <= ship.ship_class.battery_max:
				ship.current_energy = energy
			else:
				ship.current_energy = ship.ship_class.battery_max
	
	def deal_damage(self, ship: Ship, weapon: Weapon):
		ship.health -= weapon.damage
