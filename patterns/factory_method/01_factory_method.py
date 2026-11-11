from abc import ABC, abstractmethod


class AnalysisMachine(ABC):
    @abstractmethod
    def analyze(self, subject): ...


class OldAnalogMachine(AnalysisMachine):
    def analyze(self, subject) -> float:
        return 0.9 if subject.casefold() == 'rachael' else 0.3


class NewDigitalMachine(AnalysisMachine):
    def analyze(self, subject) -> float:
        return 0.95 if subject.casefold() == 'k' else 0.4


class VoightTest:
    def __init__(self, machine: AnalysisMachine) -> None:
        self._machine = machine

    def run(self, subject: str) -> bool:
        return self._machine.analyze(subject) > 0.8
