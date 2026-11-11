class AuthorizationError(Exception): ...


class NeuroInterface:
    def __init__(self) -> None:
        self.users = set()
        self.protocols = {}

    def register_user(self, user_id: str) -> None:
        self.users.add(user_id)

    def activate_protocol(self, protocol_name: str, user_id: str) -> None:
        if user_id not in self.users:
            raise AuthorizationError('Пользователь не зарегистрирован')
        self.protocols[user_id].add(protocol_name)


_interface = NeuroInterface()
register_user = _interface.register_user
activate_protocol = _interface.activate_protocol
