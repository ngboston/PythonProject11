"""
Умови:
1	Створіть абстрактний клас BankAccount, який містить:
    ◦	Поле balance (баланс).
    ◦	Абстрактний метод deposit(amount), який додає кошти на рахунок.
    ◦	Абстрактний метод withdraw(amount), який знімає кошти з рахунку.
    ◦	Метод get_balance(), який повертає поточний баланс.
2	Реалізуйте підкласи:
    ◦	SavingsAccount (ощадний рахунок), де:
    ▪	Не можна знімати більше, ніж є на рахунку.
    ▪	Додається річний відсоток (наприклад, 5%) через метод apply_interest().
    ◦	CreditAccount (кредитний рахунок), де:
    ▪	Можна піти в мінус до певного credit_limit.
    ▪	Якщо баланс негативний, знімається комісія (наприклад, 2% від боргу).
3	Створіть екземпляри SavingsAccount та CreditAccount, проведіть кілька операцій і виведіть результати.

Додаткові ускладнення:
    •	Додати логування всіх транзакцій.
    •	Реалізувати можливість переказу коштів між рахунками.
    •	Додати ще один тип рахунку, наприклад, депозитний із фіксованим

"""


from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance = 0):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    pass
    #Реалізувати клас

class CreditAccount(BankAccount):
    pass
    #Реалізувати клас