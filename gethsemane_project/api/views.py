import json

from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.http import require_http_methods

from api.ShipCombat.BLL import APIObjectFormatter
from api.ShipCombat.BLL.BattleRecorder import BattleRecorder
from api.ShipCombat.BLL.ManagerFactory import ManagerFactory
from api.ShipCombat.BLL.Xanatos import Xanatos


@require_http_methods(["GET"])
def linktest(request: HttpRequest):
	return HttpResponse(200)


@require_http_methods(["GET"])
def getship(request: HttpRequest, ship_id: int):
	ship_manager = ManagerFactory.create_ship_manager_default()
	ship = ship_manager.load_ship(ship_id)
	return JsonResponse(APIObjectFormatter.format_ship(ship))


@require_http_methods(["GET"])
def getships(request: HttpRequest, character_id: int):
	ship_manager = ManagerFactory.create_ship_manager_default()
	ships = ship_manager.load_ships_by_character_id(character_id)
	return JsonResponse(APIObjectFormatter.format_ships(ships))


@require_http_methods(["POST"])
def saveship(request: HttpRequest, character_id: int):
	ship_manager = ManagerFactory.create_ship_manager_default()
	try:
		ship_manager.create_or_update_ship(request.body, character_id)
		return HttpResponse().status_code(200)
	except Exception as err:
		return HttpResponse("Request failed: " + err.__str__())


@require_http_methods(["GET"])
def getcomponents(request: HttpRequest, character_id: int):
	component_manager = ManagerFactory.create_component_manager_default()
	components = component_manager.load_by_character_id(character_id)
	return JsonResponse(APIObjectFormatter.format_components(components))


@require_http_methods(["GET"])
def runbattle(request: HttpRequest, player_ship_id: int, opponent_ship_id: int):
	ship_manager = ManagerFactory.create_ship_manager_default()
	player_ship = ship_manager.load_ship(player_ship_id)
	opponent_ship = ship_manager.load_ship(opponent_ship_id)
	xanatos = Xanatos(player_ship, opponent_ship, BattleRecorder())
	victor = xanatos.gambit()
	return HttpResponse(victor)


@require_http_methods(["GET"])
def getshipclasses(request: HttpRequest, character_id: int):
	ship_class_manager = ManagerFactory.create_ship_class_manager_default()
	ship_classes = ship_class_manager.get_available_ship_types(character_id)
	return JsonResponse(APIObjectFormatter.format_ship_classes(ship_classes))


@require_http_methods(["GET"])
def getprogram(request: HttpRequest, program_id: int):
	program_manager = ManagerFactory.create_program_manager_default()
	program = program_manager.load_program(program_id)
	return JsonResponse(APIObjectFormatter.format_program(program))


@require_http_methods(["GET"])
def getprograms(request: HttpRequest, character_id: int):
	program_manager = ManagerFactory.create_program_manager_default()
	programs = program_manager.load_programs_by_character(character_id)
	return JsonResponse(APIObjectFormatter.format_programs(programs))


@require_http_methods(["POST"])
def saveprogram(request: HttpRequest, character_id: int):
	program_manager = ManagerFactory.create_program_manager_default()
	try:
		program_manager.save_program(json.loads(request.body), character_id)
		return HttpResponse().status_code(200)
	except Exception as err:
		return HttpResponse("Request failed: " + err.__str__())
