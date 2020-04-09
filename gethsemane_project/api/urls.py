from django.urls import path

from . import views

urlpatterns = [
	# For testing
	path('linktest/', views.linktest, name='test'),
	
	# Load all saved ships for a character
	path('character/<int:character_id>/', views.loadships),
	
	# Load all available parts for creating a ship
	path('character/<int:character_id/components/', views.loadcomponents),
	
	# TODO: Get all available ship types for creating a ship
	# path('character/<int:character_id>/shiptypes/'),
	
	# TODO: Save a new ship
	# path('character/<int:character_id/ship/'),
	
	# Load a specific, built ship
	path('ship/<int:ship_id>/', views.loadship, name='loadship'),
	
	# TODO: Load all components for a completed ship (maybe? what purpose will this serve?)
	# path('ship/<int:ship_id/components/'),
	
	# TODO: Load all subroutines for a completed ship (maybe? what purpose will this serve?)
	# path('ship/<int:ship_id>/subroutines/'),
	
	# TODO: Load cpu ship (this format needs more thought)
	# path('cpu/<int:last_battle_id>/'),
	
	# Initiate battle
	path('ship/<int:player_ship_id>/battle/<int:opponent_ship_id/', views.runbattle)
]
