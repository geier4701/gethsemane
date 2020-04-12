import json
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
from api.ShipCombat.Models.Ship import Ship
from api.ShipCombat.Models.ShipType import ShipType


def format_ship_class(ship_class: ShipType) -> json:
	formatted_ship_class = {
			"ship_class_id": ship_class.ship_type_id,
			"ship_class_name": ship_class.name,
			"weight": ship_class.weight,
			"power_gen": ship_class.power_gen,
			"battery_max": ship_class.battery_max,
			"health": ship_class.health
		}
	return json.dumps(formatted_ship_class)


def format_ship_classes(ship_classes: List[ShipType]) -> json:
	formatted_ship_classes = []
	for ship_class in ship_classes:
		formatted_ship_classes.append(format_ship_class(ship_class))
	return json.dumps(formatted_ship_classes)


def format_base_component(component: Component) -> Dict:
	return {
		"component_id": component.component_id,
		"name": component.name,
		"mass": component.mass,
		"repair_cost": component.repair_cost
	}


def format_component(component_type: str, component: Component) -> json:
	if component_type is "ammunition":
		base_component = format_base_component(component)
		component: Ammunition
		base_component["damage_type"] = component.damage_type
		base_component["ammunition_type"] = component.ammunition_type
		base_component["max_ammunition"] = component.remaining_ammo
	elif component_type is "armour":
		base_component = format_base_component(component)
		component: Armour
		base_component["armour_type"] = component.armour_type
	elif component_type is "computer":
		base_component = format_base_component(component)
		component: Computer
		base_component["speed"] = component.speed
		base_component["capacity"] = component.capacity
	elif component_type is "impulse_engine":
		base_component = format_base_component(component)
		component: ImpulseEngine
		base_component["max_accel"] = component.max_accel
		base_component["energy_cost"] = component.energy_cost
	elif component_type is "jump_drive":
		base_component = format_base_component(component)
		component: JumpDrive
		base_component["energy_cost"] = component.energy_cost
	elif component_type is "radar":
		base_component = format_base_component(component)
		component: Radar
		base_component["tracking_style"] = component.tracking_style
		base_component["energy_cost"] = component.energy_cost
	elif component_type is "weapon":
		base_component = format_base_component(component)
		component: Weapon
		base_component["range"] = component.range
		base_component["damage"] = component.damage
		base_component["ammunition_type"] = component.ammunition_type
		base_component["munition_velocity"] = component.munition_velocity
		base_component["energy_cost"] = component.energy_cost
	else:
		raise UnableToFormatException("Unknown component type given: " + component_type)
	
	return json.dumps(base_component)


def format_components(components: Dict[str, List[Component]]) -> json:
	formatted_components = []
	for component_type in components:
		for component in components[component_type]:
			formatted_components.append(format_component(component_type, component))
	
	return json.dumps(formatted_components)


def format_ship(ship: Ship) -> json:
	formatted_ship = {
		"ship_id": ship.ship_id,
		"radar": ship.radar,
		"jump_drive": ship.jump_drive,
		"impulse_engine": ship.impulse_engine,
		"computer": ship.computer,
		"coordinates": ship.coordinates,
		"ship_class": format_ship_class(ship.ship_class),
		"weapons": format_components({"weapon": ship.armament}),
		"ammunitions": format_components({"ammunition": ship.ammunitions})
	}
	return json.dumps(formatted_ship)


def format_ships(ships: List[Ship]) -> json:
	formatted_ships = []
	for ship in ships:
		formatted_ships.append(format_ship(ship))
	return json.dumps(formatted_ships)
