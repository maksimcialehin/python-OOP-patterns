from enum import Enum, auto


class AlertLevel(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()


class AlertHandler:
    def __init__(self) -> None:
        self._next: AlertHandler | None = None

    def set_next(self, handler: 'AlertHandler') -> 'AlertHandler':
        self._next = handler
        return handler

    def handle(self, alert_level: AlertLevel) -> str:
        if self._next is not None:
            return self._next.handle(alert_level)
        return f'ALERT UNASSIGNED: {alert_level.name}'


class AndroidPatrol(AlertHandler):
    def handle(self, alert_level) -> str:
        if alert_level is AlertLevel.LOW:
            return 'Патруль андроидов: Сканирование периметра с помощью тепловизора'
        return super().handle(alert_level)


class SecurityAgent(AlertHandler):
    def handle(self, alert_level) -> str:
        if alert_level is AlertLevel.MEDIUM:
            return 'Агент безопасности: исследование сектора, проверка учетных данных'
        return super().handle(alert_level)


class EliteSquad(AlertHandler):
    def handle(self, alert_level) -> str:
        if alert_level is AlertLevel.HIGH:
            return 'Элитный отряд: развертывание тактического построения, вооружение наготове'
        return super().handle(alert_level)


class SecurityDirector(AlertHandler):
    def handle(self, alert_level) -> str:
        if alert_level is AlertLevel.CRITICAL:
            return 'Директор службы безопасности: Начинаю блокировку, объявляю орбитальный удар'
        return super().handle(alert_level)


def process_alert(level: AlertLevel) -> str:
    android = AndroidPatrol()
    agent = SecurityAgent()
    elite = EliteSquad()
    director = SecurityDirector()

    android.set_next(agent).set_next(elite).set_next(director)

    return android.handle(level)
