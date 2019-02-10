from Models.Ship import Ship
from UI.ShipCreation.Computing import get_comp
from UI.ShipCreation.Impulse import get_impulse
from UI.ShipCreation.Jump import get_jump
from UI.ShipCreation.Size import get_type


def create_ship():
	ship = Ship()

	ship = get_type(ship)
	ship = get_comp(ship)
	ship = get_jump(ship)
	ship = get_impulse(ship)
