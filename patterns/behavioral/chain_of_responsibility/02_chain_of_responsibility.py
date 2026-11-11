class Handler:
    def __init__(self, successor=None) -> None:
        self.successor = successor

    def handle(self, request: str) -> str:
        if self.successor:
            return self.successor.handle(request)
        return 'Запрос не обработан'


class ConcreteHandler1(Handler):
    def handle(self, request: str) -> str:
        if 'низкий' in request.lower():
            return f'Обработчик 1 обработал: {request}'
        return super().handle(request)


class ConcreteHandler2(Handler):
    def handle(self, request: str) -> str:
        if 'высокий' in request.lower():
            return f'Обработчик 2 обработал: {request}'
        return super().handle(request)


class ConcreteHandler3(Handler):
    def handle(self, request: str) -> str:
        if 'экстренный' in request.lower():
            return f'Обработчик 3 обработал: {request}'
        return super().handle(request)


if __name__ == '__main__':
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    handler3 = ConcreteHandler3()
    handler1.successor = handler2
    handler2.successor = handler3
