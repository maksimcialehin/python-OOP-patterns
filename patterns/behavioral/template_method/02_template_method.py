from abc import ABC, abstractmethod


class Beverage(ABC):
    def template_method(self) -> None:
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()
        self.optional_step()

    def boil_water(self) -> None:
        print('Кипятим воду')

    @abstractmethod
    def brew(self) -> None:
        pass

    def pour_in_cup(self) -> None:
        print('Наливаем в чашку')

    def optional_step(self) -> None:
        ...

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

    def optional_step(self) -> None:
        print('Добавляем корицу')


class Espresso(Beverage):
    def brew(self) -> None:
        print('Варим кофе под высоким давлением')

    def add_condiments(self) -> None:
        print('Добавляем сахар')

    def optional_step(self) -> None:
        print('Процеживаем через фильтр')


e = Espresso()
e.boil_water()
e.pour_in_cup()
e.brew()
e.add_condiments()
e.optional_step()

t = Tea()
t.brew()
t.optional_step()
