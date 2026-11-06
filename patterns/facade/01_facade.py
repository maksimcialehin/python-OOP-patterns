class RobotArm:
    def collect_waste(self, garb: str) -> str:
        return f'Манипулятор собирает мусор: {garb}'


class RobotLegs:
    def move_forward(self, dest: str) -> str:
        return f'Двигатели перемещают робота вперёд к {dest}'


class RobotFacade:
    def __init__(self) -> None:
        self._robot_arm = RobotArm()
        self._robot_legs = RobotLegs()

    def clean_street(self, dest: str, garb: str) -> tuple[str, str]:
        return self._robot_legs.move_forward(dest), self._robot_arm.collect_waste(garb)
