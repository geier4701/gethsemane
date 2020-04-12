from typing import List, Dict

from api.ShipCombat.Exceptions.UnableToFormatException import UnableToFormatException
from api.ShipCombat.Models.Components.Ammunition import Ammunition
from api.ShipCombat.Models.Components.Armour import Armour
from api.ShipCombat.Models.Components.Component import Component
from api.ShipCombat.Models.Components.Computer import Computer
from api.ShipCombat.Models.Components.ImpulseEngine import ImpulseEngine
from api.ShipCombat.Models.Components.JumpDrive import JumpDrive
from api.ShipCombat.Models.Components.Radar import Radar
from api.ShipCombat.Models.Components.Weapon import Weapon
from api.ShipCombat.Models.Coordinates import Coordinates
from api.ShipCombat.Models.Ship import Ship
from api.ShipCombat.Models.ShipType import ShipType
from api.ShipCombat.Models.Subroutines.Actions.Action import Action
from api.ShipCombat.Models.Subroutines.Actions.AttemptRepairs import AttemptRepairs
from api.ShipCombat.Models.Subroutines.Actions.FireImpulse import FireImpulse
from api.ShipCombat.Models.Subroutines.Actions.FireWeapon import FireWeapon
from api.ShipCombat.Models.Subroutines.Actions.Jump import Jump
from api.ShipCombat.Models.Subroutines.Conditions.AmmunitionLevel import AmmunitionLevel
from api.ShipCombat.Models.Subroutines.Conditions.Condition import Condition
from api.ShipCombat.Models.Subroutines.Conditions.IsDisabled import IsDisabled
from api.ShipCombat.Models.Subroutines.Subroutine import Subroutine


def format_ship_class(ship_class: ShipType) -> Dict:
	formatted_ship_class = {
			"ship_class_id": ship_class.ship_type_id,
			"ship_class_name": ship_class.name,
			"weight": ship_class.weight,
			"power_gen": ship_class.power_gen,
			"battery_max": ship_class.battery_max,
			"health": ship_class.health
		}
	return formatted_ship_class


def format_ship_classes(ship_classes: List[ShipType]) -> List[Dict]:
	formatted_ship_classes = []
	for ship_class in ship_classes:
		formatted_ship_classes.append(format_ship_class(ship_class))
	return formatted_ship_classes


def format_component(component_type: str, component: Component) -> Dict:
	formatted_component = {
		"component_id": component.component_id,
		"name": component.name,
		"mass": component.mass,
		"repair_cost": component.repair_cost
	}
	
	if component_type is "ammunition":
		component: Ammunition
		formatted_component["damage_type"] = component.damage_type.name
		formatted_component["ammunition_type"] = component.ammunition_type.name
		formatted_component["max_ammunition"] = component.remaining_ammo
	elif component_type is "armour":
		component: Armour
		formatted_component["armour_type"] = component.armour_type.name
	elif component_type is "computer":
		component: Computer
		formatted_component["speed"] = component.speed
		formatted_component["capacity"] = component.capacity
	elif component_type is "impulse_engine":
		component: ImpulseEngine
		formatted_component["max_accel"] = component.max_accel
		formatted_component["energy_cost"] = component.energy_cost
	elif component_type is "jump_drive":
		component: JumpDrive
		formatted_component["energy_cost"] = component.energy_cost
	elif component_type is "radar":
		component: Radar
		formatted_component["tracking_style"] = component.tracking_style.name
		formatted_component["energy_cost"] = component.energy_cost
	elif component_type is "weapon":
		component: Weapon
		formatted_component["range"] = component.range
		formatted_component["damage"] = component.damage
		formatted_component["ammunition_type"] = component.ammunition_type.name
		formatted_component["munition_velocity"] = component.munition_velocity
		formatted_component["energy_cost"] = component.energy_cost
	else:
		raise UnableToFormatException("Unknown component type given: " + component_type)
	
	return formatted_component


def format_components(components: Dict[str, List[Component]]) -> List[Dict]:
	formatted_components = []
	for component_type in components:
		for component in components[component_type]:
			formatted_components.append(format_component(component_type, component))
	
	return formatted_components


def format_condition(condition: Condition) -> Dict:
	formatted_condition = {
		"at_least": condition.at_least,
		"at_most": condition.at_most,
		"target": condition.target.name
	}
	if condition.name is AmmunitionLevel.name:
		condition: AmmunitionLevel
		formatted_condition["ammunition_type"] = condition.ammunition_type.name
	elif condition.name is IsDisabled:
		condition: IsDisabled
		formatted_condition["component_name"] = condition.component_name
	return formatted_condition


def format_conditions(conditions: List[Condition]) -> List[Dict]:
	formatted_conditions = []
	for condition in conditions:
		formatted_conditions.append(format_condition(condition))
	return formatted_conditions


def format_coordinates(coordinates: Coordinates) -> Dict:
	formatted_coordinates = {
		"location": {
			"x": coordinates.location[0],
			"y": coordinates.location[1],
			"z": coordinates.location[2]
		},
		"speed": {
			"x": coordinates.speed[0],
			"y": coordinates.speed[1],
			"z": coordinates.speed[2]
		}
	}
	return formatted_coordinates


def format_action(action: Action) -> Dict:
	formatted_action = {
		"action_id": action.action_id,
		"name": action.name
	}
	if action.name is AttemptRepairs.name:
		action: AttemptRepairs
		formatted_action["target_component_name"] = action.target_component_name
	elif action.name is FireImpulse.name:
		action: FireImpulse
		formatted_action["velocity_change"] = format_coordinates(action.velocity_change)
	elif action.name is FireWeapon.name:
		action: FireWeapon
		formatted_action["weapon_name"] = action.weapon_name
		formatted_action["ammunition_name"] = action.ammunition_name
	elif action.name is Jump.name:
		action: Jump
		formatted_action["distance_from_enemy"] = action.distance_from_enemy
	return formatted_action


def format_actions(actions: List[Action]) -> List[Dict]:
	formatted_actions = []
	for action in actions:
		formatted_actions.append(format_action(action))
	return formatted_actions


def format_subroutine(subroutine: Subroutine) -> Dict:
	formatted_subroutine = {
		"subroutine_id": subroutine.subroutine_id,
		"priority": subroutine.priority,
		"conditions": format_conditions(subroutine.conditions),
		"actions": format_actions(subroutine.actions)
	}
	return formatted_subroutine


def format_subroutines(subroutines: List[Subroutine]) -> List[Dict]:
	formatted_subroutines = []
	for subroutine in subroutines:
		formatted_subroutines.append(format_subroutine(subroutine))
	return formatted_subroutines


def format_ship(ship: Ship) -> Dict:
	formatted_ship = {
		"ship_id": ship.ship_id,
		"radar": format_component("radar", ship.radar),
		"jump_drive": format_component("jump_drive", ship.jump_drive),
		"impulse_engine": format_component("impulse_engine", ship.impulse_engine),
		"computer": format_component("computer", ship.computer),
		"ship_class": format_ship_class(ship.ship_class),
		"weapons": format_components({"weapon": ship.armament}),
		"ammunitions": format_components({"ammunition": ship.ammunitions}),
		"subroutines": format_subroutines(ship.subroutines)
	}
	return formatted_ship


def format_ships(ships: List[Ship]) -> List[Dict]:
	formatted_ships = []
	for ship in ships:
		formatted_ships.append(format_ship(ship))
	return formatted_ships
