from django.urls import path

from . import views

urlpatterns = [
	# For testing
	path('linktest/', views.linktest),
	
	# Load all saved ships for a character
	path('character/<int:character_id>/ships/', views.getships),
	
	# Load all available parts for creating a ship
	path('character/<int:character_id>/components/', views.getcomponents),
	
	# Get all available ship types for creating a ship
	path('character/<int:character_id>/shipclasses/', views.getshipclasses),
	
	# Save or update a ship
	path('character/<int:character_id>/ship/', views.saveship),
	
	# Load a specific, built ship
	path('ship/<int:ship_id>/', views.getship),
	
	# Load program
	path('program/<int:program_id>/', views.getprogram),
	
	# Load all available programs for a character
	path('character/<int:character_id>/programs/', views.getprograms),
	
	# Save/update program
	path('character/<int:character_id>/program/', views.saveprogram),
	
	# TODO: Load cpu ship (this format needs more thought)
	# path('cpu/<int:last_battle_id>/'),
	
	# Initiate battle
	path('ship/<int:player_ship_id>/battle/<int:opponent_ship_id>/', views.runbattle)
]
