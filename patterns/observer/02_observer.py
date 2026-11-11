from collections.abc import Callable
from typing import Any


class LAPDEventBus:
    def __init__(self) -> None:
        self._events = {}

    def subscribe(self, event_type: str, callback: Callable) -> None:
        if not self._events.get(event_type):
            self._events[event_type] = []
        self._events[event_type].append(callback)

    def notify(self, event_type: str, data: Any) -> None:
        for event in self._events[event_type]:
            event(data)
