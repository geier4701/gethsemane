from typing import List

from api.ShipCombat.Models.Ship import Ship
from api.ShipCombat.Models.Subroutines.Actions.Action import Action


class Horatio:
	own_ship: Ship
	last_action: List[Action]
	enemy_intel: Ship
	
	def __init__(self, ship: Ship):
		self.own_ship = ship
		self.enemy_intel = Ship()
		self.own_ship.current_energy = self.own_ship.max_energy
	
	def command(self):
		self.own_ship.subroutines.sort(key=lambda sub: subroutine.priority)
		actions_to_take = List[Action]
		for subroutine in self.own_ship.subroutines:
			make_it_so = True
			for condition in subroutine.conditions:
				if not condition.test(self.own_ship, self.enemy_intel):
					make_it_so = False
					break
			
			if make_it_so:
				self.last_action = subroutine.actions
				actions_to_take = subroutine.actions
		
		if not actions_to_take:
			actions_to_take = self.last_action
		
		return actions_to_take
	
	def update_enemy_intel(self, enemy_intel: Ship):
		self.enemy_intel.current_energy = enemy_intel.current_energy
		self.enemy_intel.health = enemy_intel.health
		self.enemy_intel.location = enemy_intel.location
		self.enemy_intel.radar.operational = enemy_intel.radar.operational
		self.enemy_intel.jump_drive.operational = enemy_intel.jump_drive.operational
		self.enemy_intel.impulse_engine.operational = enemy_intel.impulse_engine.operational
		self.enemy_intel.computer.operational = enemy_intel.computer.operational
