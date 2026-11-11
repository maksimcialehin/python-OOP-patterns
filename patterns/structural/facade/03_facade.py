from abc import ABC, abstractmethod


class ConditionSystem(ABC):
    @abstractmethod
    def start(self, status: str) -> str: ...


class OxygenSystem(ConditionSystem):
    def start(self, status) -> str:
        return f'OXYGEN:{status}'


class ClimateControl(ConditionSystem):
    def start(self, status) -> str:
        return f'CLIMATE:{status}'


class WaterFactory(ConditionSystem):
    def start(self, status) -> str:
        return f'WATER:{status}'


class BioDomeFacade:
    def __init__(self) -> None:
        self._oxygen_system = OxygenSystem()
        self._climate_control = ClimateControl()
        self._water_factory = WaterFactory()

    def boot(self, o2_status: str, climate_status: str, water_status: str) -> tuple[str]:
        return (
            self._oxygen_system.start(o2_status),
            self._climate_control.start(climate_status),
            self._water_factory.start(water_status),
        )
