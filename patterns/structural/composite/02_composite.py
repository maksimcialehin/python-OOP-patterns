from abc import ABC, abstractmethod


class Node(ABC):
    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def contains(self, target: 'Node') -> bool:
        pass


class File(Node):
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def get_size(self) -> int:
        return self.size

    def contains(self, target: Node) -> bool:
        return False


class Directory(Node):
    def __init__(self, name: str) -> None:
        self.name = name
        self._children = []

    def add(self, node: Node) -> None:
        if node.contains(self):
            raise ValueError('Рекурсивная директория')
        self._children.append(node)

    def remove(self, node: Node) -> None:
        self._children.remove(node)

    def get_size(self) -> int:
        return sum(child.get_size() for child in self._children)

    def list_contents(self) -> list[str]:
        return [child.name for child in self._children]

    def contains(self, target: Node) -> bool:
        if self is target:
            return True
        return any(child.contains(target) for child in self._children)
