import datetime
from abc import ABC, abstractmethod


class IAccount(ABC):
    @abstractmethod
    def put(self, summa):  # Положить деньги на счет
        pass

    @abstractmethod
    def get(self, summa):  # Снять деньги со счета
        pass

    @abstractmethod
    def percent(self):  # Начислить процент
        pass


class IBonus(ABC):
    @abstractmethod
    def bonus(self):  # Начислить бонус
        pass


class BankClient(IAccount, IBonus):
    def __init__(self, name, passport, summa, year, month, day):
        self._name = name
        self._passport = passport
        self._summa_bank = summa
        self._date = datetime.date(int(year), int(month), int(day))

    @property
    def summa_bank(self):
        return self._summa_bank

    def person_display(self):
        print(f'{self._name} {self._passport} {self._summa_bank} {self._date}')

    def put(self, summa):
        self._summa_bank += summa

    def get(self, summa):
        if summa <= self._summa_bank:
            self._summa_bank -= summa

    def percent(self):
        today = datetime.date.today() - self._date
        if today == 365:
            self._summa_bank *= 1.1

    def bonus(self):
        add_bonus = 0.0
        today = datetime.date.today()
        end_of_year = datetime.date(datetime.date.today().year, 12, 31)

        if today == end_of_year:
            summa_days = end_of_year - self._date
            if self._summa_bank > 1000000 and summa_days.days > 180:
                add_bonus = self._summa_bank * 0.005
                print(f'Бонус начислен: {add_bonus}')
        return add_bonus


class ShopClient(IBonus):
    def __init__(self):
        self._summa_shop = 0
        self._summa_buy = 0

    @property
    def summa_buy(self, value):
        pass

    @summa_buy.setter
    def summa_buy(self, value):
        self._summa_buy = value

    @summa_buy.getter
    def summa_buy(self):
        return self._summa_buy

    def bonus(self):
        add_bonus = 0.0
        if self._summa_shop > 40000:
            add_bonus = self._summa_buy * 0.05
        elif self._summa_shop > 30000:
            add_bonus = self._summa_buy * 0.02
        return add_bonus

    def new_buy(self):
        self._summa_buy = int(input('Введите суму покупки: '))
        self._summa_shop += self._summa_buy
