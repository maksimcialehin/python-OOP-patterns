class PermissionError(Exception): ...


class RachaelSpy:
    @staticmethod
    def infiltrate() -> str:
        return 'Gathering intel…'

    @staticmethod
    def report() -> str:
        return 'Rachael'


class TyrellSpy:
    @staticmethod
    def infiltrate() -> str:
        return 'Hacking mainframe…'

    @staticmethod
    def report() -> str:
        return 'Tyrell Corp Agent'


class SecretSpyFactory:
    def __init__(self) -> None:
        self._valid_licenses = {'LAPD-2019', 'TyrellCorp'}
        self._spy_classes = {}

    def create_spy(self, license_key, spy_type):
        if license_key not in self._valid_licenses:
            raise PermissionError
        return self._spy_classes.get(spy_type)()

    def register_license(self, license_key: str) -> None:
        self._valid_licenses.add(license_key)

    def register_spy_type(self, spy_type: str, spy_cls) -> None:
        self._spy_classes[spy_type] = spy_cls


if __name__ == '__main__':
    spy_factory = SecretSpyFactory()
    spy_factory.register_spy_type('spy_replicant', RachaelSpy)
    spy_factory.register_spy_type('tyrell_agent', TyrellSpy)
