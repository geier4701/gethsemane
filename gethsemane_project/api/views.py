from django.http import HttpResponse

from api.ShipCombat.BLL.ShipFactory import ShipFactory
from api.ShipCombat.BLL.SubroutineFactory import SubroutineFactory
from api.ShipCombat.Repos.JumpDriveRepository import JumpDriveRepository

# Create your views here.
from api.ShipCombat.Repos.ShipRepository import ShipRepository
from api.ShipCombat.Repos.ShipTypeRepository import ShipTypeRepository
from api.ShipCombat.Repos.SubroutineRepository import SubroutineRepository


def linktest(request):
	# repo = JumpDriveRepository()
	# drive = repo.find_by_id(1)
	factory = ShipFactory(ShipRepository(), ShipTypeRepository(), SubroutineFactory(SubroutineRepository()))
	ship = factory.load_ship('First Timer')
	return ship
