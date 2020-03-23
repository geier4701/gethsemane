from abc import ABC, abstractmethod


class Action(ABC):
	action_id: int
	name: str
