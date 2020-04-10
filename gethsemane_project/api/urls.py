from django.urls import path

from . import views

urlpatterns = [
	# For testing
	path('linktest/', views.linktest),
	
	# Load all saved ships for a character
	path('character/<int:character_id>/', views.loadships),
	
	# Load all available parts for creating a ship
	path('character/<int:character_id/components/', views.loadcomponents),
	
	# Get all available ship types for creating a ship
	path('character/<int:character_id>/shipclasses/', views.getshipclasses),
	
	# Save or update a ship
	path('character/<int:character_id/ship/', views.saveship),
	
	# Load a specific, built ship
	path('ship/<int:ship_id>/', views.loadship),
	
	# TODO: Load cpu ship (this format needs more thought)
	# path('cpu/<int:last_battle_id>/'),
	
	# Initiate battle
	path('ship/<int:player_ship_id>/battle/<int:opponent_ship_id/', views.runbattle)
]
