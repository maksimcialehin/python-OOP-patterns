from abc import ABC, abstractmethod


class ModifiableWeapon(ABC):
    @abstractmethod
    def get_damage(self) -> int: ...

    @abstractmethod
    def get_modifiers(self) -> list[str]: ...


class BaseWeapon(ModifiableWeapon):
    def __init__(self, damage: int = 15) -> None:
        self.damage = damage
        self.modifiers = []

    def get_damage(self) -> int:
        return self.damage

    def get_modifiers(self) -> list:
        return self.modifiers


class BaseDecorator(ModifiableWeapon, ABC):
    def __init__(self, weapon: ModifiableWeapon) -> None:
        self._weapon = weapon

    def get_damage(self) -> int:
        return self._weapon.get_damage()

    def get_modifiers(self):
        return self._weapon.get_modifiers()


class ThermalScope(BaseDecorator):
    DAMAGE_BONUS = 5
    MODIFIER_NAME = 'thermal'

    def get_damage(self) -> int:
        return super().get_damage() + self.DAMAGE_BONUS

    def get_modifiers(self) -> list[str]:
        return [*super().get_modifiers(), self.MODIFIER_NAME]


class ExtendedBarrel(BaseDecorator):
    DAMAGE_BONUS = 10
    MODIFIER_NAME = 'extended'

    def get_damage(self) -> int:
        return super().get_damage() + self.DAMAGE_BONUS

    def get_modifiers(self) -> list[str]:
        return [*super().get_modifiers(), self.MODIFIER_NAME]


class Overclock(BaseDecorator):
    DAMAGE_BONUS = 1.3
    MODIFIER_NAME = 'overclock'

    def get_damage(self) -> int:
        return int(super().get_damage() * self.DAMAGE_BONUS)

    def get_modifiers(self) -> list[str]:
        return [*super().get_modifiers(), self.MODIFIER_NAME]


WEAPON_REGISTRY = {
    'thermal': ThermalScope,
    'extended': ExtendedBarrel,
    'overclock': Overclock,
}


class WeaponAssembly:
    def __init__(self, weapon: BaseWeapon = None) -> None:
        if weapon is None:
            weapon = BaseWeapon()
        self._weapon = weapon
        self._modifiers = weapon.get_modifiers()

    def add_modifier(self, name: str) -> None:
        self._modifiers.append(name)
        self._rebuild()

    def remove_modifier(self, name: str) -> None:
        if name not in self._modifiers:
            return
        self._modifiers.remove(name)
        self._rebuild()

    def _rebuild(self) -> None:
        self._weapon = BaseWeapon()
        for name in self._modifiers:
            weapon_decorator = WEAPON_REGISTRY.get(name)
            self._weapon = weapon_decorator(self._weapon)

    def get_stats(self) -> dict:
        return {'damage': self._weapon.get_damage(), 'modifiers': self._modifiers}
