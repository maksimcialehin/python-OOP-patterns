import json
from dataclasses import dataclass


@dataclass
class ItemDTO:
    id: int
    name: str


class FileRepository:
    filename: str
    _storage: dict

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self._load_data()

    def _load_data(self) -> None:
        try:
            with open(self.filename, 'r') as f:
                self._storage = json.loads(f.read())
        except FileNotFoundError:
            self._storage = {}

    def _save_data(self) -> None:
        with open(self.filename, 'w') as f:
            json.dump(self._storage, f, indent=2)

    def add(self, item: ItemDTO) -> None:
        self._storage[item.id] = {'name': item.name}
        self._save_data()

    def get(self, item_id: str) -> ItemDTO | None:
        item = self._storage.get(item_id)
        if item is None:
            return None
        return ItemDTO(id=item_id, name=item['name'])

    def delete(self, item_id: str) -> bool:
        if item_id in self._storage:
            del self._storage[item_id]
            self._save_data()
            return True
        return False

    def list_all(self) -> list:
        return [ItemDTO(id=k, name=v['name']) for k, v in self._storage.items()]
