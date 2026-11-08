class VirtualTerminal:
    def __init__(self, node_address: str, pool: 'TerminalPool') -> None:
        self.node_address = node_address
        self.pool = pool

    def __enter__(self) -> 'VirtualTerminal':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.pool.release(self)
        return False


class TerminalPool:
    def __init__(self, terminals_addresses: list[str]) -> None:
        self._available: list[VirtualTerminal] = [
            VirtualTerminal(node_address=address, pool=self) for address in terminals_addresses
        ]
        self._active: list[VirtualTerminal] = []

    def acquire(self) -> VirtualTerminal:
        if not self._available:
            raise ValueError('Нет доступных терминалов')
        terminal = self._available.pop(0)
        self._active.append(terminal)
        return terminal

    def release(self, terminal: VirtualTerminal) -> None:
        self._active.remove(terminal)
        self._available.append(terminal)
