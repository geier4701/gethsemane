from django.urls import path

from . import views

urlpatterns = [
	path('linktest/', views.linktest, name='test')
]
