from abc import ABC, abstractmethod


class Weapon(ABC):
    @staticmethod
    @abstractmethod
    def get_stats() -> dict: ...


class Blaster(Weapon):
    @staticmethod
    def get_stats():
        return {'name': 'Blaster', 'damage': 15, 'cost': 100}


class PlasmaKnife(Weapon):
    @staticmethod
    def get_stats():
        return {'name': 'Plasma Knife', 'damage': 25, 'cost': 250}


class ReplicantFist(Weapon):
    @staticmethod
    def get_stats():
        return {'name': 'Replicant Fist', 'damage': 10, 'cost': 0}


WEAPON_FACTORY = {
    'blaster': Blaster,
    'plasma_knife': PlasmaKnife,
    'replicant_fist': ReplicantFist,
}


def create_weapon(weapon_type: str) -> Weapon:
    weapon = WEAPON_FACTORY.get(weapon_type)
    return weapon()


def buy_weapon(credits: int, weapon_type: str) -> Weapon:
    weapon = create_weapon(weapon_type)
    stats = weapon.get_stats()
    cost = stats.get('cost')
    if credits >= cost:
        return weapon
    raise ValueError('Недостаточно кредитов')
