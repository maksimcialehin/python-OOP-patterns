import random
from abc import ABC, abstractmethod


class ReplicantState(ABC):
    @abstractmethod
    def get_strength(self, base: int) -> int: ...

    @abstractmethod
    def take_turn(self, replicant: 'Replicant') -> str: ...


class StableState(ReplicantState):
    name = 'stable'

    def get_strength(self, base: int) -> int:
        return base

    def take_turn(self, replicant: 'Replicant') -> str:
        return self.name


class CombatModeState(ReplicantState):
    name = 'combat'

    def get_strength(self, base: int) -> int:
        return int(base * 1.5)

    def take_turn(self, replicant: 'Replicant') -> str:
        replicant.hp -= 5
        if replicant.hp < 0:
            replicant.transition_to(RetiredState())
            return RetiredState.name
        return self.name


class GlitchingState(ReplicantState):
    name = 'glitching'

    def get_strength(self, base: int) -> int:
        return int(base * 0.7)

    def take_turn(self, replicant: 'Replicant') -> str:
        if random.random() < 0.2:
            replicant.transition_to(CombatModeState())
            return CombatModeState.name
        return self.name


class RetiredState(ReplicantState):
    name = 'retired'

    def get_strength(self, base: int) -> int:
        return 0

    def take_turn(self, replicant: 'Replicant') -> str:
        return self.name


class Replicant:
    def __init__(self, name: str, base_strength: int, state: ReplicantState) -> None:
        self.name = name
        self.base_strength = base_strength
        self.hp = 100
        if not state:
            state = StableState()
        self._state: ReplicantState = state

    @property
    def state(self) -> ReplicantState:
        return self._state

    def transition_to(self, state: ReplicantState) -> None:
        self._state = state

    def get_strength(self) -> int:
        return self.state.get_strength(self.base_strength)

    def take_turn(self) -> str:
        return self.state.take_turn(self)
