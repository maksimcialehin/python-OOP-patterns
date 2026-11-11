from abc import ABC, abstractmethod


class CyberImplant(ABC):
    def install(self) -> str:
        self._prepare()
        self._insert()
        self.calibrate()
        self._seal()
        self.activate()
        return self._get_result()

    def _prepare(self) -> None:
        print('sterilizing_field')

    def _insert(self) -> None:
        print('interface_connected')

    def _seal(self) -> None:
        print('synthskin_applied')

    @abstractmethod
    def calibrate(self) -> None:
        pass

    @abstractmethod
    def activate(self) -> None:
        pass

    def _get_result(self) -> str:
        return f'{self.__class__.__name__}_operational'


class NeuralLink(CyberImplant):
    def calibrate(self) -> None:
        print('synaptic_mapping_complete')

    def activate(self) -> None:
        print('neural_bridge_established')


class OpticalEnhancer(CyberImplant):
    def calibrate(self) -> None:
        print('retinal_focus_adjusted')

    def activate(self) -> None:
        print('low_light_vision_enabled')


class MuscleBooster(CyberImplant):
    def calibrate(self) -> None:
        print('myofiber_tension_set')

    def activate(self) -> None:
        print('hydraulic_response_active')
