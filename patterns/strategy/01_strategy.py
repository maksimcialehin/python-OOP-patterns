from abc import ABC, abstractmethod


class HuntAlgorithm(ABC):
    @abstractmethod
    def hunt(self, targets: list[int]) -> list[int]: ...


class VoightAlgorithm(HuntAlgorithm):
    def hunt(self, targets: list[int]) -> list[int]:
        arr = targets.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class BaselineAlgorithm(HuntAlgorithm):
    def hunt(self, targets) -> list[int]:
        if len(targets) <= 1:
            return targets.copy()
        pivot = targets[len(targets) // 2]
        left = [x for x in targets if x < pivot]
        middle = [x for x in targets if x == pivot]
        right = [x for x in targets if x > pivot]
        return self.hunt(left) + middle + self.hunt(right)


class OffWorldAlgorithm(HuntAlgorithm):
    def hunt(self, targets: list[int]) -> list[int]:
        return sorted(targets)


class BladeRunner:
    def __init__(self, algorithm: HuntAlgorithm) -> None:
        self.set_algorithm(algorithm)

    def set_algorithm(self, algorithm: HuntAlgorithm) -> None:
        self._algorithm = algorithm

    def hunt(self, targets: list[int]) -> list[int]:
        return self._algorithm.hunt(targets)
