from django.http import HttpResponse
from .ShipCombat.Repos import JumpDriveRepository

# Create your views here.


def linktest(request):
	drive = JumpDriveRepository.getJumpDriveById(1)
	return HttpResponse(drive.name)
