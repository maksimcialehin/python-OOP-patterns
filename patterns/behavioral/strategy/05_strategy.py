from abc import ABC, abstractmethod


class OpticStrategy(ABC):
    @staticmethod
    @abstractmethod
    def scan(target): ...


class ThermalOptic(OpticStrategy):
    @staticmethod
    def scan(target) -> str:
        return f'Тепловой след: {target}'


class SonarOptic(OpticStrategy):
    @staticmethod
    def scan(target) -> str:
        return f'Сонар: {target}'


class BatouEye:
    def __init__(self, strategy: OpticStrategy) -> None:
        self._strategy = strategy

    def analyze(self, target) -> None:
        return self._strategy.scan(target)
