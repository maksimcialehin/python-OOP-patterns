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


class LAPDDatabase:
    @staticmethod
    def on_fail(suspect):
        print(f'Подозреваемый добавлен: {suspect}')


class VoightDevice:
    def __init__(self, bus: LAPDEventBus):
        self._bus = bus

    def run_test(self, suspect_name, empathy_score):
        if empathy_score < 20:
            self._bus.notify('fail_test', suspect_name)


bus = LAPDEventBus()
db = LAPDDatabase()
machine = VoightDevice(bus)
bus.subscribe('fail_test', db.on_fail)
