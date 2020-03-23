from typing import List

from api.ShipCombat.Models.Coordinates import Coordinates
from api.ShipCombat.Models.Subroutines.Actions.AttemptRepairs import AttemptRepairs
from api.ShipCombat.Models.Subroutines.Actions.Delay import Delay
from api.ShipCombat.Models.Subroutines.Actions.FireImpulse import FireImpulse
from api.ShipCombat.Models.Subroutines.Actions.FireWeapon import FireWeapon
from api.ShipCombat.Models.Subroutines.Actions.Jump import Jump
from api.ShipCombat.Models.Subroutines.Actions.Scan import Scan
from api.ShipCombat.Models.Subroutines.Conditions.AmmunitionLevel import AmmunitionLevel
from api.ShipCombat.Models.Subroutines.Conditions.Distance import Distance
from api.ShipCombat.Models.Subroutines.Conditions.EnergyLevel import EnergyLevel
from api.ShipCombat.Models.Subroutines.Conditions.Health import Health
from api.ShipCombat.Models.Subroutines.Conditions.IsDisabled import IsDisabled
from api.ShipCombat.Models.Subroutines.Subroutine import Subroutine
from api.ShipCombat.Repos.ActionRepository import ActionRepository
from api.ShipCombat.Repos.ConditionRepository import ConditionRepository
from api.ShipCombat.Repos.SubroutineRepository import SubroutineRepository
from api.models import ConditionModel, ActionModel


class SubroutineFactory:
	subroutine_repo: SubroutineRepository
	
	def __init__(self, subroutine_repo: SubroutineRepository):
		self.subroutine_repo = subroutine_repo
	
	# ACTIONS
	@staticmethod
	def __build_attempt_repairs(action_model: ActionModel):
		return AttemptRepairs(action_model.action_id, action_model.component_name)
	
	@staticmethod
	def __build_delay(action_model: ActionModel):
		return Delay(action_model.action_id)
	
	@staticmethod
	def __build_fire_impulse(action_model: ActionModel):
		split_coords = action_model.component_name.split(',')
		return FireImpulse(action_model.action_id, Coordinates(0, 0, 0, int(split_coords[0]), int(split_coords[1]), int(split_coords[2])))
	
	@staticmethod
	def __build_fire_weapon(action_model: ActionModel):
		return FireWeapon(action_model.action_id, action_model.component_name, action_model.ammunition_name)
	
	@staticmethod
	def __build_jump(action_model: ActionModel):
		return Jump(action_model.action_id, int(action_model.component_name))
	
	@staticmethod
	def __build_scan(action_model: ActionModel):
		return Scan(action_model.action_id)
	
	# CONDITIONS
	@staticmethod
	def __build_ammunition_level(condition_model: ConditionModel):
		return AmmunitionLevel(condition_model.at_least, condition_model.at_most, condition_model.component_name)
	
	@staticmethod
	def __build_distance(condition_model: ConditionModel):
		return Distance(condition_model.at_least, condition_model.at_most)
	
	@staticmethod
	def __build_energy_level(condition_model: ConditionModel):
		return EnergyLevel(condition_model.at_least, condition_model.at_most, condition_model.target)
	
	@staticmethod
	def __build_health(condition_model: ConditionModel):
		return Health(condition_model.at_least, condition_model.at_most, condition_model.target)
	
	@staticmethod
	def __build_is_disabled(condition_model: ConditionModel):
		return IsDisabled(0, 0, condition_model.target, condition_model.component_name)
	
	__action_map = {
		AttemptRepairs.name: __build_attempt_repairs,
		Delay.name: __build_delay,
		FireImpulse.name: __build_fire_impulse,
		FireWeapon.name: __build_fire_weapon,
		Jump.name: __build_jump,
		Scan.name: __build_scan
	}
	
	__condition_map = {
		'AmmunitionLevel': __build_ammunition_level,
		'Distance': __build_distance,
		'EnergyLevel': __build_energy_level,
		'Health': __build_health,
		'IsDisabled': __build_is_disabled
	}
	
	def build_subroutines_for_ship(self, ship_id: int) -> List[Subroutine]:
		actions = []
		conditions = []
		subroutines = []
		subroutine_models = self.subroutine_repo.find_by_ship_id(ship_id)
		
		for subroutine_model in subroutine_models:
			action_models = ActionRepository.find_by_subroutine(subroutine_model.subroutine_id)
			condition_models = ConditionRepository.find_by_subroutine(subroutine_model.subroutine_id)
			for action_model in action_models:
				build_action = self.__action_map[action_model.name]
				actions.append(build_action(action_model))
			
			for condition_model in condition_models:
				build_condition = self.__condition_map[condition_model.name]
				conditions.append(build_condition(condition_model))
			
			subroutines.append(Subroutine(subroutine_model.subroutine_id, subroutine_model.ship.ship_id, subroutine_model.priority, conditions, actions))
		
		return subroutines
