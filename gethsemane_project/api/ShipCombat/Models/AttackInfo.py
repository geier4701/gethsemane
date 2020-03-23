from api.ShipCombat.Models.Components.Ammunition import Ammunition
from api.ShipCombat.Models.Components.Weapon import Weapon


class AttackInfo:
	weapon: Weapon
	ammo: Ammunition
	
	def __init__(self, weapon: Weapon, ammo: Ammunition):
		self.weapon = weapon
		self.ammo = ammo
