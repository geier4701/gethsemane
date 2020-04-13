from typing import Dict, List, Union

from api.ShipCombat.BLL.SubroutineFactory import SubroutineFactory
from api.ShipCombat.Models.Program import Program
from api.ShipCombat.Repos.ProgramRepository import ProgramRepository
from api.models import ProgramModel


class ProgramManager:
	program_repo: ProgramRepository
	subroutine_factory: SubroutineFactory
	
	def __init__(self, program_repo: ProgramRepository, subroutine_factory: SubroutineFactory):
		self.program_repo = program_repo
		self.subroutine_factory = subroutine_factory
	
	def load_program(self, program_id: int) -> Program:
		program = self.program_repo.find_by_id(program_id)
		subroutines = self.subroutine_factory.build_for_program(program_id)
		return Program(program_id, program.name, subroutines)
	
	def load_programs_by_character(self, character_id) -> List[Program]:
		programs = []
		program_models = self.program_repo.find_by_character_id(character_id)
		for program_model in program_models:
			subroutines = self.subroutine_factory.build_for_program(program_model.program_id)
			programs.append(Program(program_model.program_id, program_model.name, subroutines))
		return programs
	
	def build_models(self, decoded_program: Dict) -> Dict[str, Union[ProgramModel, List[dict]]]:
		program_model = ProgramModel()
		program_model.name = decoded_program['name']
		program_model.character_id = decoded_program['character_id']
		return {
			'program': program_model,
			'subroutines': self.subroutine_factory.build_models(decoded_program['subroutines'])
		}
	
	def save_program(self, program_request: Dict, character_id: int) -> None:
		program_model = ProgramModel()
		program_model.program_id = program_request['program_id']
		program_model.name = program_request['name']
		program_model.character_id = character_id
		self.program_repo.save(program_model)
		self.subroutine_factory.save_subroutines(program_request['subroutines'], program_model.program_id)
