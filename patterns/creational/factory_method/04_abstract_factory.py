from abc import ABC, abstractmethod


class LocationFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_terrain() -> dict: ...

    @staticmethod
    @abstractmethod
    def create_enemy(): ...

    @staticmethod
    @abstractmethod
    def create_hazard(): ...


class SlumsFactory(LocationFactory):
    @staticmethod
    def create_terrain():
        return 'Slums'

    @staticmethod
    def create_enemy():
        return 'Scavenger'

    @staticmethod
    def create_hazard():
        return 'Toxic Rain'


class TyrellCorpFactory(LocationFactory):
    @staticmethod
    def create_terrain():
        return 'Tyrell Corp'

    @staticmethod
    def create_enemy():
        return 'Security Bot'

    @staticmethod
    def create_hazard():
        return 'Laser Grid'


class OffWorldColonyFactory(LocationFactory):
    @staticmethod
    def create_terrain():
        return 'Off-world Colony'

    @staticmethod
    def create_enemy():
        return 'Rebel Replicant'

    @staticmethod
    def create_hazard():
        return 'Radiation'


LOCATION_REGISTRY = {
    'slums': SlumsFactory,
    'tyrell_corp': TyrellCorpFactory,
    'offworld': OffWorldColonyFactory,
}


def generate_result(loc_type: str) -> dict:
    location: LocationFactory = LOCATION_REGISTRY.get(loc_type)()
    return {
        'terrain': location.create_terrain(),
        'enemy': location.create_enemy(),
        'hazard': location.create_hazard(),
    }
