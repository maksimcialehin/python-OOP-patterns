# First-Class Functions


class Endoskeleton:
    def __init__(self, strength: int) -> None:
        self.strength = strength

    def get_strength(self) -> int:
        return self.strength


class Software:
    def __init__(self, intelligence: int) -> None:
        self.intelligence = intelligence

    def get_intelligence(self) -> int:
        return self.intelligence


replicant_factories = {
    'Nexus-6': (lambda: Endoskeleton(95), lambda: Software(80)),
    'Nexus-8': (lambda: Endoskeleton(100), lambda: Software(120)),
}


def create_replicant(model: str):
    ES_replicant, SW_replicant = replicant_factories.get(model, 'Nexus-6')
    return ES_replicant(), SW_replicant()


print(create_replicant('Nexus-6'))
