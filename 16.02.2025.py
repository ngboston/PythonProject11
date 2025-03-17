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

import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        raise NotImplementedError("Метод deposit має бути реалізований у підкласах")

    def withdraw(self, amount):
        raise NotImplementedError("Метод withdraw має бути реалізований у підкласах")

    def get_balance(self):
        return self.balance

    def _log_transaction(self, transaction):
        self.transactions.append(transaction)
        logging.info(transaction)

    def transfer(self, other_account, amount):
        if self.withdraw(amount):
            other_account.deposit(amount)
            self._log_transaction(f"Переказ {amount} на рахунок {other_account.__class__.__name__}")
            other_account._log_transaction(f"Отримано {amount} з рахунку {self.__class__.__name__}")
            return True
        return False

class SavingsAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0.05):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Внесено {amount} на ощадний рахунок")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self._log_transaction(f"Знято {amount} з ощадного рахунку")
            return True
        return False

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self._log_transaction(f"Нараховано відсотки: {interest}")

class CreditAccount(BankAccount):
    def __init__(self, balance=0, credit_limit=1000, fee_rate=0.02):
        super().__init__(balance)
        self.credit_limit = credit_limit
        self.fee_rate = fee_rate

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Внесено {amount} на кредитний рахунок")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.credit_limit:
            self.balance -= amount
            self._log_transaction(f"Знято {amount} з кредитного рахунку")
            return True
        return False

    def apply_fee(self):
        if self.balance < 0:
            fee = abs(self.balance) * self.fee_rate
            self.balance -= fee
            self._log_transaction(f"Списано комісію за кредит: {fee}")

class DepositAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0.1, term=12):
        super().__init__(balance)
        self.interest_rate = interest_rate
        self.term = term
        self.months = 0

    def deposit(self, amount):
        if amount > 0 and self.months == 0:
            self.balance += amount
            self._log_transaction(f"Внесено {amount} на депозитний рахунок")
            return True
        return False

    def withdraw(self, amount):
        if self.months == self.term and 0 < amount <= self.balance:
            self.balance -= amount
            self._log_transaction(f"Знято {amount} з депозитного рахунку")
            return True
        return False

    def pass_month(self):
        if self.months < self.term:
            self.months += 1
            if self.months == self.term:
                interest = self.balance * self.interest_rate
                self.balance += interest
                self._log_transaction(f"Нараховано відсотки за депозитом: {interest}")


savings = SavingsAccount(1000)
credit = CreditAccount(0, 1000)
deposit = DepositAccount(10000)

savings.deposit(500)
savings.withdraw(200)
savings.apply_interest()

credit.withdraw(1500)
credit.apply_fee()
credit.deposit(500)

deposit.deposit(5000)
for _ in range(12):
    deposit.pass_month()
deposit.withdraw(1000)

savings.transfer(credit, 300)

print(f"Баланс ощадного рахунку: {savings.get_balance()}")
print(f"Баланс кредитного рахунку: {credit.get_balance()}")
print(f"Баланс депозитного рахунку: {deposit.get_balance()}")