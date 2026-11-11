# Smart Reference


class RobotArm:
    def grab(self) -> str:
        return 'Механическая рука захватывает предмет'

    def release(self) -> str:
        return 'Механическая рука отпускает предмет'


class LoggingArmProxy:
    def __init__(self) -> None:
        self._arm = RobotArm()

    def grab(self) -> str:
        print("Нервный импульс вызывает метод 'grab'")
        return self._arm.grab()

    def release(self) -> str:
        print("Нервный импульс вызывает метод 'release'")
        return self._arm.release()
