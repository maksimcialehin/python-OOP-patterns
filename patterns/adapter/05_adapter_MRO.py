from abc import ABC, abstractmethod


class Powerable(ABC):
    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass


class Networkable(ABC):
    @abstractmethod
    def connect_wifi(self, ssid: str):
        pass


class BiometricReader(ABC):
    @abstractmethod
    def read_biometric(self) -> dict:
        pass


class HolographicDisplay(ABC):
    @abstractmethod
    def display_hologram(self, data: str):
        pass


class Spinner(Powerable, Networkable):
    def power_on(self) -> str:
        print('🚁 Spinner: двигатели запущены')

    def power_off(self) -> str:
        print('🚁 Spinner: посадка')

    def connect_wifi(self, ssid) -> str:
        print(f'🚁 Spinner: подключение к {ssid}')

    def get_interfaces(self) -> list[str]:
        return [cls.__name__ for cls in Spinner.__mro__[1:-2]]


class VoightDevice(Powerable, Networkable, BiometricReader):
    def power_on(self) -> str:
        print('🎛️ VD: калибровка сенсоров')

    def power_off(self) -> str:
        print('🎛️ VD: сохранение результатов')

    def connect_wifi(self, ssid) -> str:
        print(f'🎛️ VD: синхронизация с Тайрелл через {ssid}')

    def read_biometric(self) -> dict:
        return {'pupil': 0.5, 'heartbeat': 72, 'empathy': 0.3}

    def get_interfaces(self) -> list[str]:
        return [cls.__name__ for cls in VoightDevice.__mro__[1:-2]]


class HoloDeck(Powerable, HolographicDisplay):
    def power_on(self) -> str:
        print('🌌 HoloDeck: инициализация матрицы')

    def power_off(self) -> str:
        print('🌌 HoloDeck: выключение')

    def display_hologram(self, data) -> str:
        print(f"🌌 HoloDeck: проекция '{data}'")

    def get_interfaces(self) -> list[str]:
        return [cls.__name__ for cls in HoloDeck.__mro__[1:-2]]
