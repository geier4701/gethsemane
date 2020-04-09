from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from api.ShipCombat.BLL.APIObjectFormatter import APIObjectFormatter
from api.ShipCombat.BLL.BattleRecorder import BattleRecorder
from api.ShipCombat.BLL.ManagerFactory import ManagerFactory
from api.ShipCombat.BLL.Xanatos import Xanatos


@require_http_methods(["GET"])
def linktest(request):
	return HttpResponse(200)


@require_http_methods(["GET"])
def loadship(request, ship_id: int):
	ship_manager = ManagerFactory.create_ship_manager_default()
	ship = ship_manager.load_ship(ship_id)
	return JsonResponse(APIObjectFormatter.format_ship(ship))


@require_http_methods(["GET"])
def loadships(request, character_id: int):
	ship_manager = ManagerFactory.create_ship_manager_default()
	ships = ship_manager.load_ships_by_character_id(character_id)
	return JsonResponse(APIObjectFormatter.format_ships(ships))


@require_http_methods(["GET"])
def loadcomponents(request, character_id: int):
	component_manager = ManagerFactory.create_component_manager_default()
	components = component_manager.load_by_character_id(character_id)
	return JsonResponse(APIObjectFormatter.format_components(components))


@require_http_methods(["GET"])
def runbattle(request, player_ship_id: int, opponent_ship_id: int):
	ship_manager = ManagerFactory.create_ship_manager_default()
	player_ship = ship_manager.load_ship(player_ship_id)
	opponent_ship = ship_manager.load_ship(opponent_ship_id)
	xanatos = Xanatos(player_ship, opponent_ship, BattleRecorder())
	victor = xanatos.gambit()
	return HttpResponse(victor)
