from django.http import HttpResponse

# Create your views here.
from api.ShipCombat.BLL.BattleRecorder import BattleRecorder
from api.ShipCombat.BLL.ShipFactory import ShipFactory
from api.ShipCombat.BLL.SubroutineFactory import SubroutineFactory
from api.ShipCombat.BLL.Xanatos import Xanatos
from api.ShipCombat.Repos.AmmunitionRepository import AmmunitionRepository
from api.ShipCombat.Repos.ShipRepository import ShipRepository
from api.ShipCombat.Repos.ShipTypeRepository import ShipTypeRepository
from api.ShipCombat.Repos.SubroutineRepository import SubroutineRepository
from api.ShipCombat.Repos.WeaponRepository import WeaponRepository


def linktest(request):
	factory = ShipFactory(
		ShipRepository(),
		ShipTypeRepository(),
		SubroutineFactory(SubroutineRepository()),
		WeaponRepository(),
		AmmunitionRepository()
	)
	
	ship1 = factory.load_ship('First Timer')
	ship2 = factory.load_ship('Old Timer')
	
	xanatos = Xanatos(ship1, ship2, BattleRecorder())
	winner = xanatos.gambit()
	
	return HttpResponse(winner + ' wins the game!')
