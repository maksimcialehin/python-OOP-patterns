from collections.abc import Callable
from typing import Any


class EventBus:
    def __init__(self) -> None:
        self._listeners = {}

    def subscribe(self, event_type: str, listener: Callable) -> None:
        if not self._listeners.get(event_type):
            self._listeners[event_type] = []
        self._listeners[event_type].append(listener)

    def unsubscribe(self, event_type: str, listener: Callable) -> None:
        event = self._listeners.get(event_type)
        if event:
            event.remove(listener)

    def notify(self, event_type: str, data: Any) -> None:
        for listener in self._listeners[event_type]:
            listener(data)


class WallaceFactory:
    def __init__(self, bus: EventBus) -> None:
        self.bus = bus

    def create_model(self, model_name) -> None:
        print(f'Создаём {model_name}')
        self.bus.notify(event_type='new_replicant', data=model_name)
