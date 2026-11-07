from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class CitizenRecord:
    id: int = 0
    full_name: str = ''
    clearance_level: int = 0
    status: str = ''


class SurveillanceGrid:
    def __init__(self) -> None:
        self._records: dict[int, CitizenRecord] = {}
        self._seq: int = 1
        self._observers: list[Callable[[CitizenRecord, str], None]] = []

    def register_observer(self, callback: Callable[[CitizenRecord, str], None]) -> None:
        self._observers.append(callback)

    def unregister_observer(self, callback: Callable[[CitizenRecord, str], None]) -> None:
        if callback in self._observers:
            self._observers.remove(callback)

    def _notify(self, record: CitizenRecord, event: str) -> None:
        for observer in self._observers:
            observer(record, event)

    def insert(self, record: CitizenRecord) -> CitizenRecord:
        record.id = self._seq
        self._records[self._seq] = record
        self._seq += 1
        self._notify(record, 'CREATED')
        return record

    def modify(self, record: CitizenRecord) -> Optional[CitizenRecord]:
        record_id = record.id
        if record_id not in self._records:
            return None
        self._records[record_id] = record
        self._notify(record, 'UPDATED')
        return record

    def erase(self, record_id: int) -> bool:
        record = self._records.get(record_id)
        if record:
            del self._records[record_id]
            self._notify(record, 'DELETED')
            return record
        return None

    def locate(self, record_id: int) -> Optional[CitizenRecord]:
        return self._records.get(record_id)
