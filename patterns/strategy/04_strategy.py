MOVEMENT_REGISTRY = {
    'wheels': lambda: 'Еду на колесах',
    'spider': lambda: 'Ползу как паук',
    'jump': lambda: 'Прыжок',
}


class Tachikoma:
    def __init__(self, mode: str = 'wheels') -> None:
        self.mode = mode

    @property
    def mode(self) -> str:
        return self._mode

    @mode.setter
    def mode(self, value) -> None:
        self._mode = value
        self._strategy = MOVEMENT_REGISTRY.get(self._mode)

    def move(self) -> None:
        return self._strategy()
