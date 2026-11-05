class NoCyberneticEnhancement:
    def __repr__(self) -> str:
        return '<Киберимплантов нет>'


NO_ENHANCEMENTS = NoCyberneticEnhancement()


class Human:
    NO_ENHANCEMENTS = NO_ENHANCEMENTS

    def __init__(self, name: str, enhancements: list[str] = NO_ENHANCEMENTS) -> None:
        self.name = name
        if enhancements is not self.NO_ENHANCEMENTS:
            enhancements = enhancements.copy()
        self.enhancements = enhancements

    def has_enhancements(self) -> bool:
        return self.enhancements is not self.NO_ENHANCEMENTS
