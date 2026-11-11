from typing import Any


class AccessHandler:
    def __init__(self) -> None:
        self._next: AccessHandler | None = None

    def __or__(self, other: 'AccessHandler') -> 'AccessHandler':
        self._next = other
        return other

    def __ror__(self, other: Any) -> 'AccessHandler':
        return self

    def check_access(self, credentials: dict, level: int) -> str:
        if self._next:
            return self._next.check_access(credentials, level)
        return 'ACCESS DENIED: Insufficient credentials'


class PublicAccess(AccessHandler):
    def check_access(self, credentials, level) -> str:
        if level == 1:
            return 'ACCESS GRANTED: Public dossier'
        return super().check_access(credentials, level)


class RestrictedAccess(AccessHandler):
    def check_access(self, credentials, level) -> str:
        clearance = credentials.get('clearance', 0)
        if level == 2 and clearance >= 2:
            return 'ACCESS GRANTED: Restricted files'
        return super().check_access(credentials, level)


class ConfidentialAccess(AccessHandler):
    def check_access(self, credentials, level) -> str:
        clearance = credentials.get('clearance', 0)
        biometric = credentials.get('biometric')
        if level == 3 and clearance >= 3 and biometric:
            return 'ACCESS GRANTED: Confidential data'
        return super().check_access(credentials, level)


class TopSecretAccess(AccessHandler):
    def check_access(self, credentials, level) -> str:
        clearance = credentials.get('clearance', 0)
        biometric = credentials.get('biometric')
        neural_hash = credentials.get('neural_hash')
        if level == 4 and clearance >= 3 and biometric and int(str(neural_hash), 16) == 0x4F2A:
            return 'ACCESS GRANTED: Omega protocols'
        return super().check_access(credentials, level)


def get_access(credentials: dict, level: int) -> str:
    public = PublicAccess()
    restricted = RestrictedAccess()
    confidential = ConfidentialAccess()
    top_secret = TopSecretAccess()

    public | restricted | confidential | top_secret

    return public.check_access(credentials, level)


if __name__ == '__main__':
    credentials = {'clearance': 3, 'biometric': True, 'neural_hash': 0x9999}
    print(get_access(credentials, 3))
