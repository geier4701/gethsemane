class Character:
	character_id: int
	user_id: int
	first_name: str
	last_name: str
	
	def __init__(self, character_id: int, user_id: int, first_name: str, last_name: str):
		self.character_id = character_id
		self.user_id = user_id
		self.first_name = first_name
		self.last_name = last_name
