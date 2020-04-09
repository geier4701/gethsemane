from typing import Dict, List

from api.ShipCombat.Models.Components.Ammunition import Ammunition
from api.ShipCombat.Models.Components.Armour import Armour
from api.ShipCombat.Models.Components.Component import Component
from api.ShipCombat.Models.Components.Computer import Computer
from api.ShipCombat.Models.Components.ImpulseEngine import ImpulseEngine
from api.ShipCombat.Models.Components.JumpDrive import JumpDrive
from api.ShipCombat.Models.Components.Radar import Radar
from api.ShipCombat.Models.Components.Weapon import Weapon
from api.ShipCombat.Repos.AmmunitionRepository import AmmunitionRepository
from api.ShipCombat.Repos.ArmourRepository import ArmourRepository
from api.ShipCombat.Repos.ComputerRepository import ComputerRepository
from api.ShipCombat.Repos.ImpulseEngineRepository import ImpulseEngineRepository
from api.ShipCombat.Repos.JumpDriveRepository import JumpDriveRepository
from api.ShipCombat.Repos.RadarRepository import RadarRepository
from api.ShipCombat.Repos.WeaponRepository import WeaponRepository


class ComponentManager:
	armour_repo: ArmourRepository
	computer_repo: ComputerRepository
	impulse_repo: ImpulseEngineRepository
	jump_repo: JumpDriveRepository
	radar_repo: RadarRepository
	weapon_repo: WeaponRepository
	ammo_repo: AmmunitionRepository
	
	def __init__(
			self,
			armour_repo: ArmourRepository,
			computer_repo: ComputerRepository,
			impulse_repo: ImpulseEngineRepository,
			jump_repo: JumpDriveRepository,
			radar_repo: RadarRepository,
			weapon_repo: WeaponRepository,
			ammo_repo: AmmunitionRepository
		):
		self.armour_repo = armour_repo
		self.computer_repo = computer_repo
		self.impulse_repo = impulse_repo
		self.jump_repo = jump_repo
		self.radar_repo = radar_repo
		self.weapon_repo = weapon_repo
		self.ammo_repo = ammo_repo
	
	def load_by_character_id(self, character_id: int) -> Dict[str, List[Component]]:
		armours = []
		armour_models = self.armour_repo.find_by_character_id(character_id)
		for armour_model in armour_models:
			armours.append(Armour(armour_model))
		
		computers = []
		computer_models = self.computer_repo.find_by_character_id(character_id)
		for computer_model in computer_models:
			computers.append(Computer(computer_model))
		
		impulse_engines = []
		impulse_models = self.impulse_repo.find_by_character_id(character_id)
		for impulse_model in impulse_models:
			impulse_engines.append(ImpulseEngine(impulse_model))
		
		jump_drives = []
		jump_models = self.jump_repo.find_by_character_id(character_id)
		for jump_model in jump_models:
			jump_drives.append(JumpDrive(jump_model))
		
		radars = []
		radar_models = self.radar_repo.find_by_character_id(character_id)
		for radar_model in radar_models:
			radars.append(Radar(radar_model))
		
		weapons = []
		weapon_models = self.weapon_repo.find_by_character_id(character_id)
		for weapon_model in weapon_models:
			weapons.append(Weapon(weapon_model))
		
		ammos = []
		ammo_models = self.ammo_repo.find_by_character_id(character_id)
		for ammo_model in ammo_models:
			ammos.append(Ammunition(ammo_model))
		
		components = {
			'armours': armours,
			'computers': computers,
			'impulse_engines': impulse_engines,
			'jump_drives': jump_drives,
			'radars': radars,
			'weapons': weapons,
			'ammos': ammos
		}
		return components
