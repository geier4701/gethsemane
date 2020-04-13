from typing import List

from api.ShipCombat.Models.Subroutines.Subroutine import Subroutine


class Program:
	program_id: int
	subroutines: List[Subroutine]
	
	def __init__(self, program_id: int, subroutines: List[Subroutine]):
		self.program_id = program_id
		self.subroutines = subroutines
