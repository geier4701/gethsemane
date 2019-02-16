from Location import Location
from Ship import Ship
from Subroutines.Actions.Action import Action
from Weapon import Weapon


class FireWeapon(Action):
	own_ship: Ship
	weapon: Weapon
	coordinates: Location
	
	def __init__(self, own_ship: Ship, weapon: Weapon, coordinates: Location):
		self.own_ship = own_ship
		self.weapon = weapon
		self.coordinates = coordinates
	
	weapon_to_use = own_ship.armament[weapon.id]
	weapon_to_use.fire(coordinates)
