from typing import List

from api.ShipCombat.BLL.BattleRecorder import BattleRecorder
from api.ShipCombat.BLL.Horatio import Horatio
from api.ShipCombat.Models import Ship
from api.ShipCombat.Models.Components.Weapon import Weapon
from api.ShipCombat.Models.Subroutines.Actions.Action import Action
from api.ShipCombat.Models.Subroutines.Actions.FireWeapon import FireWeapon
from api.ShipCombat.Models.Subroutines.Actions.Scan import Scan


class Xanatos:
	player_ship: Ship
	opponent_ship: Ship
	battle_recorder: BattleRecorder
	
	def __init__(self, player: Ship, opponent: Ship, battle_recorder: BattleRecorder):
		self.player_ship = player
		from api.ShipCombat.Models.Coordinates import Coordinates
		self.player_ship.coordinates = Coordinates(100, 100, 100, 0, 0, 0)
		self.opponent_ship = opponent
		self.opponent_ship.coordinates = Coordinates(-100, -100, -100, 0, 0, 0)
		self.battle_recorder = battle_recorder
	
	def gambit(self) -> str:
		player_captain = Horatio(self.player_ship, self.battle_recorder)
		opponent_captain = Horatio(self.opponent_ship, self.battle_recorder)
		
		round_count = 0
		while self.player_ship.health > 0 and self.opponent_ship.health > 0 and round_count < 100:
			self.generate_energy()
			self.move_ships()
			# Faster computer goes first?
			self.engage(player_captain.command(), player_captain, opponent_captain)
			self.engage(opponent_captain.command(), opponent_captain, player_captain)
			
			player_captain.reset_ship_weapons()
			opponent_captain.reset_ship_weapons()
			round_count += 1
		
		if round_count == 100:
			victor = 'DRAW'
		elif self.player_ship.health > 0:
			victor = 'player'
		else:
			victor = 'cpu'
		
		self.battle_recorder.export_battle(victor)
		return victor
	
	def engage(self, actions: List[Action], captain: Horatio, enemy_captain: Horatio):
		for action in actions:
			action_result = captain.own_ship.activate(action)
			targeted_coordinates = None
			if isinstance(action, FireWeapon):
				targeted_coordinates = captain.enemy_intel.coordinates
				# TODO: Track weapons / Check enemy ship speed as well as location
				if (
						action_result.ammo is not None
						and action_result.weapon is not None
						and captain.enemy_intel.coordinates.location == enemy_captain.own_ship.coordinates.location
						and captain.enemy_intel.coordinates.speed == enemy_captain.own_ship.coordinates.speed
				):
					self.deal_damage(enemy_captain.own_ship, action_result.weapon)
			if isinstance(action, Scan) and action_result is True:
				captain.update_enemy_intel(enemy_captain.own_ship)
			self.battle_recorder.record_action(action_result, captain.own_ship, action, targeted_coordinates)
	
	def generate_energy(self):
		ships = [self.player_ship, self.opponent_ship]
		for ship in ships:
			energy = ship.current_energy + ship.power_gen
			if energy <= ship.battery_max:
				ship.current_energy = energy
			else:
				ship.current_energy = ship.battery_max
	
	def move_ships(self):
		ships = [self.player_ship, self.opponent_ship]
		for ship in ships:
			loc = 0
			while loc < 3:
				ship.coordinates.location[loc] += ship.coordinates.speed[loc]
				loc += 1
	
	# MAYBE THIS SHOULD BE TAKE_DAMAGE() ON THE SHIP
	def deal_damage(self, ship: Ship, weapon: Weapon):
		# TODO: Implement armour
		ship.health -= weapon.damage
