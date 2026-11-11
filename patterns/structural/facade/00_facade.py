class PowerDomain:
    @staticmethod
    def allocate(district: str, amount: int) -> bool:
        if amount > 300:
            print(f'[PowerDomain] ОШИБКА: Превышен лимит мощности для {district}!')
            return False
        print(f'[PowerDomain] Выделено {amount} МВт для {district}.')
        return True


class BankGateway:
    @staticmethod
    def charge(account: str, amount: int) -> bool:
        if account == 'BROKE_ACC':
            print(f'[BankGateway] ОШИБКА: Недостаточно средств на счете {account}!')
            return False
        print(f'[BankGateway] Успешно списано {amount} ед. со счета {account}.')
        return True


class BillboardController:
    @staticmethod
    def set_status(message: str):
        print(f'[Billboard] Рекламные щиты переключены на: {message}')


class CityGridFacade:
    def __init__(self):
        self.power_domain = PowerDomain()
        self.bank = BankGateway()
        self.billboard = BillboardController()

    def provide_energy(self, district: str, account: str, power_amount: int, cost: int) -> None:
        is_enough_energy = self.power_domain.allocate(district, power_amount)
        if is_enough_energy:
            is_enough_money = self.bank.charge(account, cost)

            if is_enough_money:
                self.billboard.set_status(f'Энергия подана в {district}')
            else:
                self.billboard.set_status('Ошибка оплаты')
        else:
            self.billboard.set_status('ВНИМАНИЕ: БЛЭКАУТ')
