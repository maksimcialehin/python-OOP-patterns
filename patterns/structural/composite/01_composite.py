from abc import ABC, abstractmethod


class Equipment(ABC):
    @abstractmethod
    def get_power_consumption(self) -> int: ...


class SimpleEquipment(Equipment):
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def get_power_consumption(self) -> int:
        return self.power


class ComplexEquipment(Equipment):
    def __init__(self, name: str) -> None:
        self.name = name
        self.storage: list[Equipment] = []

    def add(self, equipment: Equipment) -> None:
        self.storage.append(equipment)

    def remove(self, equipment: Equipment) -> None:
        self.storage.remove(equipment)

    def get_power_consumption(self) -> int:
        return sum(equip.get_power_consumption() for equip in self.storage)
