from api.ShipCombat.Models.Character import Character
from api.models import CharacterModel


class CharacterRepository:
	def find_by_id(self, character_id: str) -> Character:
		return CharacterModel.objects.get(character_id=character_id)
