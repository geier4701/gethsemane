from django.http import HttpResponse
from api.ShipCombat.Repos.JumpDriveRepository import JumpDriveRepository

# Create your views here.


def linktest(request):
	repo = JumpDriveRepository()
	drive = repo.find_by_id(1)
	return HttpResponse(drive.name)
