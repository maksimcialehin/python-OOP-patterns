class CyberImplant:
    def __init__(self) -> None:
        self.model: str | None = None
        self.material: str | None = None
        self.power_level: int = 10

    def __repr__(self):
        return f'CyberImplant(model={self.model}, material={self.material}, power={self.power_level})'


class ImplantBuilder:
    def __init__(self) -> None:
        self.cyber_implant = CyberImplant()

    def set_model(self, model: str) -> 'ImplantBuilder':
        self.cyber_implant.model = model
        return self

    def set_material(self, material: str) -> 'ImplantBuilder':
        self.cyber_implant.material = material
        return self

    def set_power(self, power: int) -> 'ImplantBuilder':
        self.cyber_implant.power_level = power
        return self

    def build(self) -> CyberImplant:
        if self.cyber_implant.model is None or self.cyber_implant.material is None:
            raise ValueError('Модель или материал не заданы')
        return self.cyber_implant
