from collections.abc import Callable
from typing import Any


class LAPDEventBus:
    def __init__(self) -> None:
        self._listeners = {}

    def subscribe(self, event_type: str, listener: Callable) -> None:
        if not self._listeners.get(event_type):
            self._listeners[event_type] = []
        self._listeners[event_type].append(listener)

    def unsubscribe(self, event_type: str, listener: Callable):
        event = self._listeners.get(event_type)
        if event:
            event.remove(listener)

    def notify(self, event_type: str, data: Any) -> None:
        for listener in self._listeners[event_type]:
            listener(data)
