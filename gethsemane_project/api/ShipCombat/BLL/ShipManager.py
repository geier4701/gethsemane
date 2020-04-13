import json
from typing import List

from api.ShipCombat.BLL.ProgramManager import ProgramManager
from api.ShipCombat.BLL.ShipValidator import ShipValidator
from api.ShipCombat.Exceptions.FailedToSaveException import FailedToSaveException
from api.ShipCombat.Models.Components.Ammunition import Ammunition
from api.ShipCombat.Models.Components.Computer import Computer
from api.ShipCombat.Models.Components.ImpulseEngine import ImpulseEngine
from api.ShipCombat.Models.Components.JumpDrive import JumpDrive
from api.ShipCombat.Models.Components.Radar import Radar
from api.ShipCombat.Models.Components.Weapon import Weapon
from api.ShipCombat.Models.Ship import Ship
from api.ShipCombat.Models.ShipType import ShipType
from api.ShipCombat.Repos.AmmunitionRepository import AmmunitionRepository
from api.ShipCombat.Repos.ShipRepository import ShipRepository
from api.ShipCombat.Repos.WeaponRepository import WeaponRepository
from api.models import WeaponModel, AmmunitionModel, ShipModel, ProgramModel


class ShipManager:
	ship_repo: ShipRepository
	weapon_repo: WeaponRepository
	ammo_repo: AmmunitionRepository
	ship_validator: ShipValidator
	program_manager: ProgramManager
	
	def __init__(
			self,
			ship_repo: ShipRepository,
			weapon_repo: WeaponRepository,
			ammo_repo: AmmunitionRepository,
			ship_validator: ShipValidator,
			program_manager: ProgramManager
	):
		self.ship_repo = ship_repo
		self.weapon_repo = weapon_repo
		self.ammo_repo = ammo_repo
		self.ship_validator = ship_validator
		self.program_manager = program_manager
	
	def load_ship(self, ship_id: int) -> Ship:
		ship_model = self.ship_repo.find_by_id(ship_id)
		return self.build_ship(ship_model)
	
	def load_ships_by_character_id(self, character_id: int) -> List[Ship]:
		ships = []
		ship_models = self.ship_repo.find_by_character_id(character_id)
		for ship_model in ship_models:
			ships.append(self.build_ship(ship_model))
		
		return ships
	
	def create_or_update_ship(self, ship_request: json, character_id: int) -> None:
		decoded_ship = json.loads(ship_request)
		
		ship_model = ShipModel()
		ship_model.character_id = character_id
		ship_model.ship_id = decoded_ship['ship_id']
		ship_model.name = decoded_ship['name']
		ship_model.radar_id = decoded_ship['radar_id']
		ship_model.jump_drive_id = decoded_ship['jump_drive_id']
		ship_model.impulse_engine_id = decoded_ship['impulse_engine_id']
		ship_model.computer_id = decoded_ship['computer_id']
		ship_model.ship_type_id = decoded_ship['ship_class_id']
		
		weapon_models = []
		for weapon in decoded_ship['weapons']:
			weapon_models.append(self.weapon_repo.find_by_id(weapon['weapon_id']))
		
		ammo_models = []
		for ammo in decoded_ship['ammunitions']:
			ammo_models.append(self.ammo_repo.find_by_id(ammo['ammunition_id']))
		
		self.ship_validator.validate_ship(ship_model)
		
		if self.program_manager.build_models(decoded_ship['program']) is not None:
			decoded_program = self.program_manager.build_models(decoded_ship['program'])
		else:
			decoded_program = None
		
		try:
			if decoded_program is not None:
				self.program_manager.save_program(decoded_program, ship_model.character_id)
				ship_model.program_id = decoded_program['program'].program_id
			else:
				ship_model.program_id = None
			
			self.ship_repo.save_ship(ship_model, weapon_models, ammo_models)
		except Exception as err:
			raise FailedToSaveException(err.__str__())
	
	def build_ship(self, ship_model: ShipModel) -> Ship:
		ship = Ship()
		ship.ship_id = ship_model.ship_id
		ship.name = ship_model.name
		ship.ship_class = ShipType(ship_model.ship_type)
		ship.radar = Radar(ship_model.radar)
		ship.jump_drive = JumpDrive(ship_model.jump_drive)
		ship.impulse_engine = ImpulseEngine(ship_model.impulse_engine)
		ship.computer = Computer(ship_model.computer)
		
		weapon_models: List[WeaponModel]
		weapon_models = self.weapon_repo.find_by_ship_id(ship_model.ship_id)
		for weapon_model in weapon_models:
			ship.armament.append(Weapon(weapon_model))
		
		ammo_models: List[AmmunitionModel]
		ammo_models = self.ammo_repo.find_by_ship_id(ship_model.ship_id)
		for ammo_model in ammo_models:
			ship.ammunitions.append(Ammunition(ammo_model))
		
		if ship_model.program is not None:
			ship.program = self.program_manager.load_program(ship_model.program.program_id)
		else:
			ship.program = None
		
		return ship
