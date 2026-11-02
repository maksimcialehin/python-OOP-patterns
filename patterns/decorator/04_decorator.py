from abc import ABC, abstractmethod


class Modifiable(ABC):
    @abstractmethod
    def get_damage(self) -> int: ...

    @abstractmethod
    def get_cost(self) -> int: ...


class BaseWeapon(Modifiable):
    def __init__(self, damage: int = 15, cost: int = 0) -> None:
        self.damage = damage
        self.cost = cost

    def get_damage(self) -> int:
        return self.damage

    def get_cost(self) -> int:
        return self.cost


class WeaponDecorator(BaseWeapon):
    def __init__(self, weapon: Modifiable) -> None:
        self._weapon = weapon

    def get_damage(self) -> int:
        return self._weapon.get_damage()

    def get_cost(self) -> int:
        return self._weapon.get_cost()


class ThermalScope(WeaponDecorator):
    DAMAGE_BONUS = 5
    COST_BONUS = 50

    def get_damage(self) -> int:
        return super().get_damage() + self.DAMAGE_BONUS

    def get_cost(self) -> int:
        return super().get_cost() + self.COST_BONUS


class ExtendedBarrel(WeaponDecorator):
    DAMAGE_BONUS = 10
    COST_BONUS = 100

    def get_damage(self) -> int:
        return super().get_damage() + self.DAMAGE_BONUS

    def get_cost(self) -> int:
        return super().get_cost() + self.COST_BONUS


class Overclock(WeaponDecorator):
    DAMAGE_BONUS = 1.3
    COST_BONUS = 200

    def get_damage(self) -> int:
        return int(super().get_damage() * self.DAMAGE_BONUS)

    def get_cost(self) -> int:
        return super().get_cost() + self.COST_BONUS


WEAPON_REFISTRY = {
    'thermal': ThermalScope,
    'extended': ExtendedBarrel,
    'overclock': Overclock,
}


def build_weapon(modifiers: list[str]) -> Modifiable:
    weapon: Modifiable = BaseWeapon()
    for modifier in modifiers:
        weapon = WEAPON_REFISTRY.get(modifier)(weapon)
    return weapon


weapon: Modifiable = build_weapon(''.split())
print(weapon.get_damage())
print(weapon.get_cost())
