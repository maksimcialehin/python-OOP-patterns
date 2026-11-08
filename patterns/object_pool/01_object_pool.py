class QuantumCore:
    def __init__(self, core_id: int):
        self.core_id = core_id
        self.is_active = False


class CorePool:
    _available: list[QuantumCore]
    _in_use: list[QuantumCore]

    def __init__(self, cores: list[QuantumCore]) -> None:
        self._available = cores
        self._in_use = []

    def acquire(self) -> QuantumCore | None:
        if not self._available:
            return None
        core = self._available.pop()
        if core:
            core.is_active = True
            self._in_use.append(core)
        return core

    def release(self, core: QuantumCore) -> None:
        core.is_active = False
        self._available.append(core)
        self._in_use.remove(core)
