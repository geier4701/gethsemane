from abc import ABC


class Action(ABC):
	action_id: int
	name: str
	# TODO: Add complexity to use up computer capacity
