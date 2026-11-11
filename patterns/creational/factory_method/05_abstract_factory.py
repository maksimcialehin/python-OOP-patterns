from abc import ABC, abstractmethod


class WeaponComponentFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_barrel(barrel_type: str) -> str: ...

    @staticmethod
    @abstractmethod
    def create_scope(scope_type: str) -> str: ...

    @staticmethod
    @abstractmethod
    def create_ammo(ammo_type: str) -> str: ...

    @staticmethod
    @abstractmethod
    def create_damage(damage_type: int) -> int: ...


class SniperFactory(WeaponComponentFactory):
    @staticmethod
    def create_barrel(barrel_type):
        if barrel_type not in ('Long-range barrel'):
            raise ValueError('Невозможно собрать оружие')
        return barrel_type

    @staticmethod
    def create_scope(scope_type):
        if scope_type not in ('Thermal scope', 'Holographic scope'):
            raise ValueError('Невозможно собрать оружие')
        return scope_type

    @staticmethod
    def create_ammo(ammo_type):
        if ammo_type not in ('AP rounds', 'Incendiary rounds'):
            raise ValueError('Невозможно собрать оружие')
        return ammo_type

    @staticmethod
    def create_damage(damage_type):
        if damage_type not in (50, 75, 100):
            raise ValueError('Невозможно собрать оружие')
        return damage_type


class AssaultFactory(WeaponComponentFactory):
    @staticmethod
    def create_barrel(barrel_type):
        if barrel_type not in ('Short barrel', 'Heavy barrel'):
            raise ValueError('Невозможно собрать оружие')
        return barrel_type

    @staticmethod
    def create_scope(scope_type):
        if scope_type not in ('Red dot', 'Iron sights'):
            raise ValueError('Невозможно собрать оружие')
        return scope_type

    @staticmethod
    def create_ammo(ammo_type):
        if ammo_type not in ('Plasma cells', 'Tracer rounds'):
            raise ValueError('Невозможно собрать оружие')
        return ammo_type

    @staticmethod
    def create_damage(damage_type):
        if damage_type not in (10, 15, 20):
            raise ValueError('Невозможно собрать оружие')
        return damage_type


WEAPONS = {
    'sniper': SniperFactory,
    'assault': AssaultFactory,
}


def assemble_weapon(config: dict) -> dict:
    gun_type = config.get('type')
    gun: WeaponComponentFactory = WEAPONS.get(gun_type)()
    try:
        return {
            'barrel': gun.create_barrel(config.get('barrel')),
            'scope': gun.create_scope(config.get('scope')),
            'ammo': gun.create_ammo(config.get('ammo')),
            'damage': gun.create_damage(config.get('damage')),
        }
    except Exception as exc:
        raise exc
