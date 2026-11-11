from abc import ABC, abstractmethod


class HeroLike(ABC):
    @abstractmethod
    def attack(self, target: str) -> int:
        pass

    @abstractmethod
    def is_alive(self) -> bool:
        pass


class Hero(HeroLike):
    def __init__(self, name: str, damage: int, hp: int):
        self.name = name
        self._damage = damage
        self.hp = hp

    def attack(self, target: str) -> int:
        return self._damage

    def is_alive(self) -> bool:
        return self.hp > 0


class CombatUnit(ABC):
    @abstractmethod
    def deal_damage(self) -> int:
        pass

    @abstractmethod
    def is_alive(self) -> bool:
        pass


class AlienRobot(CombatUnit):
    def __init__(self, power: int, integrity: int):
        self._power = power
        self._integrity = integrity

    def deal_damage(self) -> int:
        return self._power

    def is_alive(self) -> bool:
        return self._integrity > 0


class HeroToCombatUnitAdapter(CombatUnit):
    def __init__(self, hero: HeroLike) -> None:
        self._hero = hero

    def deal_damage(self) -> int:
        return self._hero.attack('target')

    def is_alive(self) -> bool:
        return self._hero.is_alive()


class CombatUnitToHeroAdapter(HeroLike):
    def __init__(self, unit: CombatUnit) -> None:
        self._unit = unit

    def attack(self, target: str) -> int:
        return self._unit.deal_damage()

    def is_alive(self) -> bool:
        return self._unit.is_alive()
