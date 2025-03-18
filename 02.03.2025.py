import datetime

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.log_file = "transactions.log"

    def deposit(self, amount):
        raise NotImplementedError("Метод deposit повинен бути реалізований у підкласах")

    def withdraw(self, amount):
        raise NotImplementedError("Метод withdraw повинен бути реалізований у підкласах")

    def get_balance(self):
        return self.balance

    def _log_transaction(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as f:
            f.write(f"[{timestamp}] {message}\n")


class SavingsAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0.05):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        self._log_transaction(f"Депозит на ощадний рахунок: +{amount}, баланс: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self._log_transaction(f"Зняття з ощадного рахунку: -{amount}, баланс: {self.balance}")
        else:
            self._log_transaction(f"Недостатньо коштів для зняття: {amount}, баланс: {self.balance}")

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self._log_transaction(f"Нараховано відсотки: +{interest}, баланс: {self.balance}")


class CreditAccount(BankAccount):
    def __init__(self, balance=0, credit_limit=1000, fee_rate=0.02):
        super().__init__(balance)
        self.credit_limit = credit_limit
        self.fee_rate = fee_rate

    def deposit(self, amount):
        self.balance += amount
        self._log_transaction(f"Депозит на кредитний рахунок: +{amount}, баланс: {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount >= -self.credit_limit:
            self.balance -= amount
            self._log_transaction(f"Зняття з кредитного рахунку: -{amount}, баланс: {self.balance}")
            if self.balance < 0:
                fee = abs(self.balance) * self.fee_rate
                self.balance -= fee
                self._log_transaction(f"Комісія за кредит: -{fee}, баланс: {self.balance}")
        else:
            self._log_transaction(f"Перевищено кредитний ліміт: {amount}, баланс: {self.balance}")

class DepositAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0.1, term_months=12):
        super().__init__(balance)
        self.interest_rate = interest_rate
        self.term_months = term_months
        self.start_date = datetime.date.today()
        self.end_date = self.start_date + datetime.timedelta(days=30 * term_months)
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            self._log_transaction(f"Депозит на депозитний рахунок: +{amount}, баланс: {self.balance}")
        else:
            self._log_transaction(f"Рахунок не активний. Неможливо поповнити.")

    def withdraw(self, amount):
        if self.is_active:
            if datetime.date.today() >= self.end_date:
                if amount <= self.balance:
                    self.balance -= amount
                    self._log_transaction(f"Зняття з депозитного рахунку: -{amount}, баланс: {self.balance}")
                else:
                    self._log_transaction(f"Недостатньо коштів для зняття: {amount}, баланс: {self.balance}")
            else:
                self._log_transaction(f"Рахунок не активний. Зняття неможливе до {self.end_date}.")
        else:
            self._log_transaction(f"Рахунок не активний. Зняття неможливе.")

    def apply_interest(self):
        if self.is_active and datetime.date.today() >= self.end_date:
            interest = self.balance * self.interest_rate
            self.balance += interest
            self._log_transaction(f"Нараховано відсотки по депозиту: +{interest}, баланс: {self.balance}")
            self.is_active = False

def transfer_funds(from_account, to_account, amount):
    if from_account.get_balance() >= amount:
        from_account.withdraw(amount)
        to_account.deposit(amount)
        from_account._log_transaction(f"Переказ коштів на інший рахунок: -{amount}, баланс: {from_account.get_balance()}")
        to_account._log_transaction(f"Отримання коштів з іншого рахунку: +{amount}, баланс: {to_account.get_balance()}")
    else:
        from_account._log_transaction(f"Недостатньо коштів для переказу: {amount}, баланс: {from_account.get_balance()}")

savings = SavingsAccount(1000)
credit = CreditAccount(0)
deposit = DepositAccount(10000)

savings.deposit(500)
savings.withdraw(200)
savings.apply_interest()

credit.withdraw(1500)
credit.deposit(500)

transfer_funds(savings, credit, 300)
transfer_funds(savings, deposit, 100)

print(f"Ощадний рахунок: {savings.get_balance()}")
print(f"Кредитний рахунок: {credit.get_balance()}")
print(f"Депозитний рахунок: {deposit.get_balance()}")