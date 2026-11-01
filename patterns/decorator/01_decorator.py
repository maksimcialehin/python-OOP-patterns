from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def fire() -> int: ...


class BaseBlaster(Weapon):
    def __init__(self, base_damage: int) -> None:
        self._damage = base_damage

    def fire(self) -> int:
        return self._damage


class WeaponDecorator(Weapon):
    def __init__(self, weapon: Weapon) -> None:
        self._weapon = weapon

    def fire(self) -> int:
        return self._weapon.fire()


class ThermalScope(WeaponDecorator):
    def fire(self) -> int:
        return super().fire() + 5


class ExtendedBarrel(WeaponDecorator):
    def fire(self) -> int:
        return super().fire() + 10


class OverheatPenalty(WeaponDecorator):
    def fire(self) -> int:
        return int(super().fire() / 2)


def calculate_damage(
    base_damage: int,
    has_thermal_scope: bool,
    has_extended_barrel: bool,
    is_overheated: bool,
):
    blaster = BaseBlaster(base_damage)
    if has_thermal_scope:
        blaster = ThermalScope(blaster)
    if has_extended_barrel:
        blaster = ExtendedBarrel(blaster)
    if is_overheated:
        blaster = OverheatPenalty(blaster)
    return blaster.fire()


print(calculate_damage(10, 1, 1, 0))
