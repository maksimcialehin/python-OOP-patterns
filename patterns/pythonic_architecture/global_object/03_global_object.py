import threading


class ResourceManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.energy: int = 1000
            cls.water: int = 500
            cls.lock = threading.Lock()
        return cls._instance

    def allocate(self, amount_energy: int, amount_water: int) -> bool:
        with self.lock:
            if self.energy < amount_energy or self.water < amount_water:
                return False
            self.energy -= amount_energy
            self.water -= amount_water
        return True

    def report(self) -> dict[str, int]:
        with self.lock:
            energy = self.energy
            water = self.water
        return {
            'energy': energy,
            'water': water,
        }
