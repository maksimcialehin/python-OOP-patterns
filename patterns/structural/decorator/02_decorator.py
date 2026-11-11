from abc import ABC, abstractmethod


class Replicant(ABC):
    @abstractmethod
    def get_strength(self) -> int: ...


class Nexus6Base(Replicant):
    def __init__(self, strength: int = 80) -> None:
        self._strength = strength

    def get_strength(self) -> int:
        return self._strength


class ReplicantDecorator(Replicant):
    def __init__(self, creature: Replicant) -> None:
        self._creature = creature

    def get_strength(self) -> int:
        return self._creature.get_strength()


class StrengthChip(ReplicantDecorator):
    def get_strength(self) -> int:
        return super().get_strength() + 20


class AgilityChip(ReplicantDecorator):
    def get_strength(self) -> int:
        return int(super().get_strength() * 1.2)


class FaultyWiring(ReplicantDecorator):
    def get_strength(self) -> int:
        return int(super().get_strength() * 0.7)


MODIFIER_REGISTRY = {
    'strength': StrengthChip,
    'agility': AgilityChip,
    'faulty': FaultyWiring,
}


def build_replicant(modifiers: list[str]) -> Replicant:
    replicant = Nexus6Base()
    for modifier in modifiers:
        rpl_decorator = MODIFIER_REGISTRY.get(modifier)
        replicant = rpl_decorator(replicant)
    return replicant


repl: Nexus6Base = build_replicant('strength'.split())
print(repl.get_strength())
