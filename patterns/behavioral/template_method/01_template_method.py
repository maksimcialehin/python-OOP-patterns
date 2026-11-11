from abc import ABC, abstractmethod


class Beverage(ABC):
    def template_method(self) -> None:
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self) -> None:
        print('Кипятим воду')

    @abstractmethod
    def brew(self) -> None:
        pass

    def pour_in_cup(self) -> None:
        print('Наливаем в чашку')

    @abstractmethod
    def add_condiments(self) -> None:
        pass


class Tea(Beverage):
    def brew(self) -> None:
        print('Завариваем чайный лист')

    def add_condiments(self) -> None:
        print('Добавляем лимон и сахар')


class Coffee(Beverage):
    def brew(self) -> None:
        print('Варим кофейные зёрна')

    def add_condiments(self) -> None:
        print('Добавляем молоко и сахар')
