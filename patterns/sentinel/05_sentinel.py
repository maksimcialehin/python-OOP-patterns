class Sentinel:
    def __init__(self, name) -> None:
        self._name = name

    def __repr__(self) -> str:
        return f'<sentinel {self._name}>'


class SentinelFactory:
    _sentinels = {}

    @classmethod
    def create(cls, name: str) -> Sentinel:
        return cls._sentinels.setdefault(name, Sentinel(name))
