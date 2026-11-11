# VirtualProxy


class NavigationCore:
    def __init__(self) -> None:
        print('Ядро навигации инициализировано: потребление энергии 40%')
        self.status = 'active'

    def calculate_route(self, destination: str) -> str:
        return f"Маршрут к '{destination}' построен"


class NavigationProxy:
    def __init__(self) -> None:
        self._core = None

    def calculate_route(self, destination: str) -> None:
        if self._core is None:
            self._core = NavigationCore()
        return self._core.calculate_route(destination)
