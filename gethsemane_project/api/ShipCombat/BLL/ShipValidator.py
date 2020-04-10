from api.ShipCombat.Exceptions.ShipValidationException import ShipValidationException
from api.models import ShipModel


# TODO: Complete ship validation
class ShipValidator:
	def __validate_weight(self, ship_model: ShipModel) -> bool:
		pass
	
	def __validate_components_owned(self, ship_model: ShipModel) -> bool:
		pass
	
	def validate_ship(self, ship_model: ShipModel) -> None:
		if not self.__validate_weight(ship_model):
			raise ShipValidationException('Ship over weight limit')
		if not self.__validate_components_owned(ship_model):
			raise ShipValidationException('Component used that character does not own')
