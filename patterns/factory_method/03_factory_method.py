from abc import ABC, abstractmethod


class Replicant(ABC):
    @staticmethod
    @abstractmethod
    def get_specs() -> dict: ...


class Nexus6(Replicant):
    @staticmethod
    def get_specs():
        return {'model': 'Nexus-6', 'strength': 80, 'lifespan': 4}


class Nexus7(Replicant):
    @staticmethod
    def get_specs():
        return {'model': 'Nexus-7', 'strength': 90, 'lifespan': 6}


class Nexus8(Replicant):
    @staticmethod
    def get_specs():
        return {'model': 'Nexus-8', 'strength': 100, 'lifespan': 10}


REPLICANT_REGISTRY = {
    'Nexus-6': Nexus6,
    'Nexus-7': Nexus7,
    'Nexus-8': Nexus8,
}


def build_replicant(model: str):
    return REPLICANT_REGISTRY.get(model)
