class PermissionError(Exception): ...


class CyberImplant:
    def upgrade(self) -> str:
        return 'Имплант обновлён'


class SecureLoggingImplantProxy:
    def __init__(self, user: str, password: str) -> None:
        self.user_name = user
        self.password = password
        self._implant = CyberImplant()

    def upgrade(self) -> str:
        if self.user_name != 'admin' or self.password != 'secret_key':
            print('Обнаружена попытка взлома! Сообщаю администратору…')
            raise PermissionError('Неправильный логин/пароль')
        print(f'Добро пожаловать {self.user_name}! Начинаю обновление…')
        return self._implant.upgrade()
