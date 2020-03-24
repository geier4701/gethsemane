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
			self.generate_energy()
			self.move_ships()
			# Faster computer goes first?
			self.engage(player_captain.command(), player_captain, opponent_captain)
			self.engage(opponent_captain.command(), opponent_captain, player_captain)
			player_captain.reset_ship_weapons()
			opponent_captain.reset_ship_weapons()
		
		# RETURN VICTOR AND BATTLE REPORT
	
	def engage(self, actions, captain: Horatio, enemy_captain: Horatio, info=None):
		for action in actions:
			action_result = captain.own_ship.activate(action)
			if action is FireWeapon:
				# TODO: Track weapons / Check enemy ship speed as well as location
				if action_result.ammo is not None and action_result.weapon is not None and captain.enemy_intel.coordinates.location == enemy_captain.own_ship.coordinates:
					self.deal_damage(enemy_captain.own_ship, action_result.weapon)
			if action is Scan and action_result is True:
				captain.update_enemy_intel(enemy_captain.own_ship)
	
	def generate_energy(self):
		ships = [self.player_ship, self.opponent_ship]
		for ship in ships:
			energy = ship.current_energy + ship.ship_class.power_gen
			if energy <= ship.ship_class.battery_max:
				ship.current_energy = energy
			else:
				ship.current_energy = ship.ship_class.battery_max
	
	def move_ships(self):
		ships = [self.player_ship, self.opponent_ship]
		for ship in ships:
			loc = 0
			while loc < 3:
				ship.location.location[loc] += ship.location.speed[loc]
				loc += 1
	
	# MAYBE THIS SHOULD BE TAKE_DAMAGE() ON THE SHIP
	def deal_damage(self, ship: Ship, weapon: Weapon):
		# TODO: Implement armour
		ship.health -= weapon.damage
