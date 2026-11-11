class CityGridStatusError(Exception): ...


class GlobalCitySettings:
    _instance = None
    ALLOWED_STATUSES = {'online', 'offline', 'critical'}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.population = 0
            cls._instance._energy_grid_status = 'online'
        return cls._instance

    @property
    def energy_grid_status(self):
        return self._energy_grid_status

    @energy_grid_status.setter
    def energy_grid_status(self, value):
        if value not in self.ALLOWED_STATUSES:
            raise CityGridStatusError('Неправильный статус сети')
        self._energy_grid_status = value
