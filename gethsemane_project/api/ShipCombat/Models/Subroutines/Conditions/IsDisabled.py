from api.ShipCombat.Models.Subroutines.Conditions.Condition import Condition, Target


class IsDisabled(Condition):
	component_name: str
	
	def __init__(self, at_least: int, at_most: int, target: Target, component_name: str):
		self.at_least = at_least
		self.at_most = at_most
		self.target = target
		self.component_name = component_name
		
	def test(self, own_ship, enemy_ship):
		named_components = own_ship.get_components()[self.component_name]
		if hasattr(named_components, "__len__"):
			for component in named_components:
				if component.operational is False:
					return True
			return False
		
		else:
			return named_components.operational
