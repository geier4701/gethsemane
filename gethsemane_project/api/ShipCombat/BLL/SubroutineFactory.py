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
	def build_attempt_repairs(action_model: ActionModel):
		return AttemptRepairs(action_model.action_id, action_model.component_name)
	
	@staticmethod
	def build_delay(action_model: ActionModel):
		return Delay(action_model.action_id)
	
	@staticmethod
	def build_fire_impulse(action_model: ActionModel):
		integers = action_model.component_name.split(',')
		return FireImpulse(action_model.action_id, Coordinates(integers[0], integers[1], integers[2]))
	
	@staticmethod
	def build_fire_weapon(action_model: ActionModel):
		return FireWeapon(action_model.action_id, action_model.component_name, action_model.ammunition_name)
	
	@staticmethod
	def build_jump(action_model: ActionModel):
		return Jump(action_model.action_id, action_model.component_name)
	
	@staticmethod
	def build_scan(action_model: ActionModel):
		return Scan(action_model.action_id, action_model.component_name)
	
	# CONDITIONS
	@staticmethod
	def build_ammunition_level(condition_model: ConditionModel):
		return AmmunitionLevel(condition_model.at_least, condition_model.at_most, condition_model.component_name)
	
	@staticmethod
	def build_distance(condition_model: ConditionModel):
		return Distance(condition_model.at_least, condition_model.at_most)
	
	@staticmethod
	def build_energy_level(condition_model: ConditionModel):
		return EnergyLevel(condition_model.at_least, condition_model.at_most, condition_model.target)
	
	@staticmethod
	def build_health(condition_model: ConditionModel):
		return Health(condition_model.at_least, condition_model.at_most, condition_model.target)
	
	@staticmethod
	def build_is_disabled(condition_model: ConditionModel):
		return IsDisabled(0, 0, condition_model.target, condition_model.component_name)
	
	action_map = {
		'AttemptRepairs': build_attempt_repairs,
		'Delay': build_delay,
		'FireImpulse': build_fire_impulse,
		'FireWeapon': build_fire_weapon,
		'Jump': build_jump,
		'Scan': build_scan
	}
	
	condition_map = {
		'AmmunitionLevel': build_ammunition_level,
		'Distance': build_distance,
		'EnergyLevel': build_energy_level,
		'Health': build_health,
		'IsDisabled': build_is_disabled
	}
	
	def build_subroutines_for_ship(self, ship_id: int):
		actions = []
		conditions = []
		subroutines = []
		subroutine_models = self.subroutine_repo.find_by_ship_id(ship_id)
		
		for subroutine_model in subroutine_models:
			action_models = ActionRepository.find_by_subroutine(subroutine_model.subroutine_id)
			condition_models = ConditionRepository.find_by_subroutine(subroutine_model.subroutine_id)
			for action_model in action_models:
				build_action = self.action_map[action_model.name]
				actions.append(build_action(action_model))
			
			for condition_model in condition_models:
				build_condition = self.condition_map[condition_model.name]
				conditions.append(build_condition(condition_model))
			
			subroutines.append(Subroutine(subroutine_model.subroutine_id, subroutine_model.ship.ship_id, subroutine_model.priority, conditions, actions))
		
		return subroutines
