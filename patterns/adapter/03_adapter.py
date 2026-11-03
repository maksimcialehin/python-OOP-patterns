import json
from abc import ABC, abstractmethod


class TyrellDatabase:
    def __init__(self):
        self._data = {
            'N6-123': [
                {'model': 'Nexus-6', 'incept_date': '2019-01-01', 'status': 'retired'},
            ],
            'N7-456': [
                {'model': 'Nexus-7', 'incept_date': '2021-06-15', 'status': 'active'},
            ],
            'N8-789': [
                {'model': 'Nexus-8', 'incept_date': '2023-03-10', 'status': 'active'},
            ],
            'N6-999': [
                {'model': 'Nexus-6', 'incept_date': '2018-11-20', 'status': 'retired'},
                {'model': 'Nexus-6', 'incept_date': '2018-11-20', 'status': 'active'},  # Дубликат
            ],
        }

    def query_by_serial(self, serial: str) -> list:
        return self._data.get(serial, [])


class ReplicantRepository(ABC):
    @abstractmethod
    def find_by_id(self, sid: str) -> dict:
        pass


class TyrellDBAdapter(ReplicantRepository):
    def __init__(self, tyrell_db: TyrellDatabase) -> None:
        self._db = tyrell_db

    @staticmethod
    def _process_query(query: list):
        try:
            query = query[0]
            status = query.get('status')
            res = {
                'model': query.get('model'),
                'active': status != 'retired',
            }
        except:
            return
        else:
            return res

    def find_by_id(self, sid):
        res = {'model': 'UNKNOWN', 'active': False}
        query = self._db.query_by_serial(serial=sid)
        if query:
            res = self._process_query(query)
        return res
