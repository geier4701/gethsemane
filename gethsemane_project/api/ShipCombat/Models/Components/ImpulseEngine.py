from .Component import Component


class ImpulseEngine(Component):
	max_accel: int
	energy_cost: int
	
	def __init__(self, component_id: int, name: str, mass: int, energy_cost: int, repair_cost: int, max_accel: int):
		self.component_id = component_id
		self.name = name
		self.mass = mass
		self.energy_cost = energy_cost
		self.repair_cost = repair_cost
		self.max_accel = max_accel
		self.operational = True
	
	def get_stat_info(self):
		return {
			"id": self.component_id,
			"name": self.name,
			"mass": self.mass,
			"energy_cost": self.energy_cost,
			"max_accel": self.max_accel
		}

# a few ways to go about it. 1. no generating power. All  battery operated ships, ensuring that they need to manage
# energy as a resource. 2. power generation tied to ship class. You don't get to pick how much power is generated a
# turn, but you can devote extra weight to batteries if you want. 3. You must pick different power plants depending on
# how much power you want to generate each turn. or,4. no batteries, only a generation amount. You get your power
# every turn and that's it, with no way to store it for later. Works with either pick a power plant or tied to ship
# class methods
