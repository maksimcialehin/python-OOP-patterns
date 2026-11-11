def brute_force_protocol():
    return 'Взлом грубой силой!'


def ghost_hack_protocol():
    return 'Призрачный взлом...'


class Cyberdeck:
    def __init__(self, protocol_name: str):
        self._tools = {
            'brute': brute_force_protocol,
            'ghost': ghost_hack_protocol,
        }
        self._tool = self._tools.get(protocol_name)

    def breach(self) -> str:
        return self._tool()
