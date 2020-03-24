from typing import List

from api.ShipCombat.BLL.SubroutineFactory import SubroutineFactory
from api.ShipCombat.Models.Components.Ammunition import Ammunition
from api.ShipCombat.Models.Components.Computer import Computer
from api.ShipCombat.Models.Components.ImpulseEngine import ImpulseEngine
from api.ShipCombat.Models.Components.JumpDrive import JumpDrive
from api.ShipCombat.Models.Components.Radar import Radar
from api.ShipCombat.Models.Components.Weapon import Weapon
from api.ShipCombat.Models.Ship import Ship
from api.ShipCombat.Repos.AmmunitionRepository import AmmunitionRepository
from api.ShipCombat.Repos.ShipRepository import ShipRepository
from api.ShipCombat.Repos.WeaponRepository import WeaponRepository
from api.models import WeaponModel, AmmunitionModel
from api.ShipCombat.Repos.ShipTypeRepository import ShipTypeRepository


class ShipFactory:
	ship_repo: ShipRepository
	ship_type_repo: ShipTypeRepository
	subroutine_factory: SubroutineFactory
	weapon_repo: WeaponRepository
	ammo_repo: AmmunitionRepository
	
	def __init__(
			self,
			ship_repo: ShipRepository,
			ship_type_repo: ShipTypeRepository,
			subroutine_factory: SubroutineFactory,
			weapon_repo: WeaponRepository,
			ammo_repo: AmmunitionRepository
	):
		self.ship_repo = ship_repo
		self.ship_type_repo = ship_type_repo
		self.subroutine_factory = subroutine_factory
		self.weapon_repo = weapon_repo
		self.ammo_repo = ammo_repo
	
	def load_ship(self, ship_name: str):
		ship_model = self.ship_repo.find_by_name(ship_name)[0]
		
		ship = Ship()
		ship.name = ship_model.name
		ship.ship_class = ship_model.ship_type.name
		ship.radar = Radar(ship_model.radar)
		ship.jump_drive = JumpDrive(ship_model.jump_drive)
		ship.impulse_engine = ImpulseEngine(ship_model.impulse_engine)
		ship.computer = Computer(ship_model.computer)
		ship.battery_max = ship_model.ship_type.battery_max
		ship.power_gen = ship_model.ship_type.power_gen
		ship.health = ship_model.ship_type.health
		ship.weight = ship_model.ship_type.weight
		
		weapon_models: List[WeaponModel]
		weapon_models = self.weapon_repo.find_by_ship_id(ship_model.ship_id)
		for weapon_model in weapon_models:
			ship.armament.append(Weapon(weapon_model))
		
		ammo_models: List[AmmunitionModel]
		ammo_models = self.ammo_repo.find_by_ship_id(ship_model.ship_id)
		for ammo_model in ammo_models:
			ship.ammunitions.append(Ammunition(ammo_model))
		
		ship.subroutines = self.subroutine_factory.build_subroutines_for_ship(ship_model.ship_id)
		
		return ship
	
	def create_ship(self):
		pass
	
	def update_ship(self, created_ship: Ship):
		pass
