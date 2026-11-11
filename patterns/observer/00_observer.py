class AudioSystem:
    @staticmethod
    def play_beep():
        print('[Audio] Проигрывание: beep.mp3')


class BlackMarketAPI:
    @staticmethod
    def order_stims():
        print('[DarkWeb] Заказано стимуляторов: 1 шт.')


class AdrenalinePump:
    """Этот класс жестко завязан на внешние системы"""

    def __init__(self):
        self.stims_left = 3
        self._observers = []

    def subscribe(self, callback):
        self._observers.append(callback)

    def heartbeat_drop(self):
        print('[Имплант] Внимание! Критическое падение пульса.')
        if self.stims_left > 0:
            self.stims_left -= 1
            print(f'[Имплант] Впрыск адреналина! Осталось: {self.stims_left}')

            for callback in self._observers:
                callback()
        else:
            print('[Имплант] Нет стимуляторов!')
