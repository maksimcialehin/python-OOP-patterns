from abc import ABC, abstractmethod


class MemoryAlgorithm(ABC):
    @abstractmethod
    def process(memories: list[int]) -> list[int]: ...


class ImplantAlgorithm(MemoryAlgorithm):
    @staticmethod
    def process(memories: list[int]) -> list[int]:
        return sorted(memories)


class OrganicAlgorithm(MemoryAlgorithm):
    @staticmethod
    def process(memories: list[int]) -> list[int]:
        return sorted(x for x in memories if x % 2 == 0) + sorted(x for x in memories if x % 2 != 0)


class EraseAlgorithm(MemoryAlgorithm):
    @staticmethod
    def process(memories: list[int]) -> list[int]:
        return memories[::-1]


class MemoryProcessor:
    def __init__(self, algorithm) -> None:
        self.set_algorithm(algorithm)

    def set_algorithm(self, algorithm: MemoryAlgorithm) -> None:
        self._algorithm = algorithm

    def process(self, targets: list[int]) -> list[int]:
        return self._algorithm.process(targets)
