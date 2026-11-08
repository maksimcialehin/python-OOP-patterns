smg = lambda: 'Стрельба из ПП'
plasma_rifle = lambda: 'Стрельба из плазменного ружья'
rpg = lambda: 'Запуск ракеты'
nothing = lambda: 'Ближний бой'

WEAPON_REGISTRY = {
    'smg': smg,
    'plasma_rifle': plasma_rifle,
    'rpg': rpg,
    'nothing': nothing,
}

thermoptic = lambda: 'Невидимость включена'
simple_camo = lambda: 'Упрощённый камуфляж'
nothing = lambda: 'Без камуфляжа'

CAMO_REGISTRY = {
    'thermoptic': thermoptic,
    'simple_camo': simple_camo,
    'nothing': nothing,
}


class Motoko:
    def __init__(self, weapon: str = 'smg', camo: str = 'thermoptic') -> None:
        self._weapon = weapon
        self._camo = camo

    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, value: str):
        self._weapon = WEAPON_REGISTRY.get(value, 'smg')

    @property
    def camo(self):
        return self._camo

    @camo.setter
    def camo(self, value: str):
        self._camo = CAMO_REGISTRY.get(value, 'thermoptic')

    def engage(self) -> tuple[str, str]:
        return (self._camo(), self._weapon())
