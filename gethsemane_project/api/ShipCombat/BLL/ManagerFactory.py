from api.ShipCombat.BLL.ComponentManager import ComponentManager
from api.ShipCombat.BLL.ShipManager import ShipManager
from api.ShipCombat.BLL.SubroutineFactory import SubroutineFactory
from api.ShipCombat.Repos.AmmunitionRepository import AmmunitionRepository
from api.ShipCombat.Repos.ArmourRepository import ArmourRepository
from api.ShipCombat.Repos.ComputerRepository import ComputerRepository
from api.ShipCombat.Repos.ImpulseEngineRepository import ImpulseEngineRepository
from api.ShipCombat.Repos.JumpDriveRepository import JumpDriveRepository
from api.ShipCombat.Repos.RadarRepository import RadarRepository
from api.ShipCombat.Repos.ShipRepository import ShipRepository
from api.ShipCombat.Repos.ShipTypeRepository import ShipTypeRepository
from api.ShipCombat.Repos.SubroutineRepository import SubroutineRepository
from api.ShipCombat.Repos.WeaponRepository import WeaponRepository


class ManagerFactory:
	@staticmethod
	def create_ship_manager_default() -> ShipManager:
		return ShipManager(
			ShipRepository(),
			ShipTypeRepository(),
			SubroutineFactory(SubroutineRepository()),
			WeaponRepository(),
			AmmunitionRepository()
		)
	
	@staticmethod
	def create_component_manager_default() -> ComponentManager:
		return ComponentManager(
			ArmourRepository(),
			ComputerRepository(),
			ImpulseEngineRepository(),
			JumpDriveRepository(),
			RadarRepository(),
			WeaponRepository(),
			AmmunitionRepository()
		)
