from abc import ABC, abstractmethod


class ThermalSignature(ABC):
    @abstractmethod
    def get_value(self) -> int: ...


class BaseSignature(ThermalSignature):
    LOWER_LIMIT = 0

    def __init__(self, visibility: int = 100) -> None:
        self._visibility = visibility

    def get_value(self) -> int:
        return max(self.LOWER_LIMIT, self._visibility)


class SignatureDecorator(ThermalSignature):
    def __init__(self, signature: ThermalSignature) -> None:
        self._signature = signature

    def get_value(self) -> int:
        return self._signature.get_value()


class RainMasking(SignatureDecorator):
    BUFF = 10

    def get_value(self) -> int:
        return max(0, super().get_value() - self.BUFF)


class SmokeScreen(SignatureDecorator):
    BUFF = 15

    def get_value(self) -> int:
        return max(0, super().get_value() - self.BUFF)


class ActiveCamouflage(SignatureDecorator):
    BUFF = 5

    def get_value(self) -> int:
        return max(0, int(super().get_value() / self.BUFF))


SIGNATURE_REGISTRY = {
    'rain': RainMasking,
    'smoke': SmokeScreen,
    'camouflage': ActiveCamouflage,
}


def build_signature(modifiers: list[str]) -> ThermalSignature:
    signature = BaseSignature()
    for modifier in modifiers:
        signature = SIGNATURE_REGISTRY.get(modifier)(signature)
    return signature


repl: BaseSignature = build_signature('rain'.split())
print(repl.get_value())
