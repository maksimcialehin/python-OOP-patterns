from abc import ABC, abstractmethod
from typing import Optional


class Component(ABC):
    @abstractmethod
    def render(self, indent: int = 0) -> str:
        pass

    @abstractmethod
    def find_by_title(self, title: str) -> Optional['Component']:
        pass


class Text(Component):
    def __init__(self, content: str) -> None:
        self.content = content

    def render(self, indent: int = 0) -> str:
        return ' ' * indent + self.content

    def find_by_title(self, title) -> Optional['Component']:
        if title == self.content:
            return self
        return None


class Button(Component):
    def __init__(self, label: str) -> None:
        self.label = label

    def render(self, indent: int = 0) -> str:
        return ' ' * indent + f'< {self.label} >'

    def find_by_title(self, title) -> Optional['Component']:
        if title == self.label:
            return self
        return None


class Panel(Component):
    title: str
    _children: list[Component]

    def __init__(self, title: str) -> None:
        self.title = title
        self._children = []

    def add(self, component: Component) -> None:
        self._children.append(component)

    def remove(self, component: Component) -> None:
        self._children.remove(component)

    def render(self, indent: int = 0) -> str:
        string_elements = [' ' * indent + f'[ {self.title} ]'] + [
            child.render(indent=indent + 2) for child in self._children
        ]
        return '\n'.join(string_elements)

    def find_by_title(self, title) -> Component | None:
        if self.title == title:
            return self
        for child in self._children:
            res = child.find_by_title(title)
            if res is not None:
                return res
        return None
