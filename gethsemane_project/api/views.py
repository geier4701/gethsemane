from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def linktest(request):
	return HttpResponse('test success')
