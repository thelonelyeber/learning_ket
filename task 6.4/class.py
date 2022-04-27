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
    def __init__(self, name, passport, summa_bank, date):
        self._name = name
        self._passport = passport
        self._summa_bank = summa_bank
        self._date = date

    @property
    def summa_bank(self):
        return self._summa_bank

    def person_display(self):
        print(f'{self._name} {self._passport} {self._summa_bank} {self._date}')

    def bank_client(self):
        pass

    def put(self, summa):
        self._summa_bank += summa

    def get(self, summa):
        if summa <= self._summa_bank:
            self._summa_bank -= summa

    def percent(self):
        date = self._date.split('-')
        today = datetime.date.today() - datetime.date(int(date[0]), int(date[1]), int(date[2]))
        if today == 365:
            self._summa_bank *= 1.1

    def bonus(self):
        add_bonus = 0.0


class ShopClient(IBonus):
    def __init__(self, summa_shop, summa_buy):
        self._summa_shop = summa_shop
        self._summa_buy = summa_buy

    @property
    def summa_buy(self):
        return

    def shop_client(self):
        pass

    def new_buy(self):
        pass
