class BankAccount:

    def __init__(self, name, initial_balance=0, currency="UAH"):
        self.name = name
        self.balance = initial_balance
        self.currency = currency

    def info(self):
        return f"Account Name: {self.name}, Balance: {self.balance} {self.currency}"

account1 = BankAccount("Alice")
account2 = BankAccount("Bob", 1000)
account3 = BankAccount("Charlie", 500, "USD")

print(account1.info())
print(account2.info())
print(account3.info())

class BankAccount:
    def __init__(self, name, initial_balance=0, currency="UAH"):
        self.name = name
        self.balance = initial_balance
        self.currency = currency
        self.transactions = []

    def deposit(self, amount, comment=None):
        if isinstance(amount, list):
            for amt in amount:
                self.balance += amt
        if comment:
            self.transactions.append((amt, comment))
        else:
            self.transactions.append((amt, "Deposit"))
            self.balance += amount
        if comment:
            self.transactions.append((amount, comment))
        else:
            self.transactions.append((amount, "Deposit"))


    def current_balance(self):
        return self.balance

account1 = BankAccount("Alice")
account1.deposit(100)
account1.deposit([50, 200, 300])
account1.deposit(500, "Salary")

print(account1.current_balance())
print(account1.transactions)

class BankAccount:
    def __init__(self, name, initial_balance=0, currency="UAH"):
        self.name = name
        self.balance = initial_balance
        self.currency = currency
        self.transactions = []


    def withdraw(self, amount, currency=None):
        if isinstance(amount, list):
            for amt in amount:
                self.balance -= amt
                self.transactions.append((amt, "Withdraw"))
         elif currency:
                    exchange_rate = 40
            if currency == "USD":
                self.balance -= amount * exchange_rate
                self.transactions.append((amount, "Withdraw in USD"))
                else:
                    self.balance -= amount
                    self.transactions.append((amount, "Withdraw"))
                else:
                    self.balance -= amount
                    self.transactions.append((amount, "Withdraw"))

account1 = BankAccount("Alice", 1000)
account1.withdraw(100) # снятие 100
account1.withdraw(50, "USD") # снятие 50 в USD
account1.withdraw([20, 30, 50]) # снятие списком

print(account1.current_balance()) # Вывод текущего баланса

class BankAccount:

    def __init__(self, name, initial_balance=0, currency="UAH"):


    def deposit(self, amount, comment=None):
# (описание метода deposit)

    def withdraw(self, amount, currency=None):
# (описание метода withdraw)

    def transfer(self, amount, target_account, comment=None):
        if isinstance(amount, list):
            for amt in amount:
                self.withdraw(amt)
                target_account.deposit(amt, comment)
        else:
            self.withdraw(amount)
            target_account.deposit(amount, comment)

# Примеры использования
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

account1.transfer(200, account2) # перевод 200 на счет Bob

print(account1.current_balance()) # Баланс Alice
print(account2.current_balance()) # Баланс Bob

class BankAccount:

    def __init__(self, owner, balance=0, currency="USD"):
        self.owner = owner
        self.balance = balance
        self.currency = currency
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount} {self.currency}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f'Withdrew: {amount} {self.currency}')
        else: print("Insufficient funds!")

    def transfer(self, amount, other_account):
            if amount <= self.balance:
                self.withdraw(amount)
                other_account.deposit(amount)
                self.transaction_history.append(f'Transferred: {amount} {other_account.currency} to {other_account.owner}')
            else: print("Insufficient funds!")

    def get_account_info(self, detailed=False, as_dict=False):
        info = { 'Owner': self.owner, 'Balance': self.balance, 'Currency': self.currency }
         if detailed: info['Transaction History'] = self.transaction_history info['Transaction Count'] = len(self.transaction_history)
         if as_dict:
             return info
         else:
                return f"Owner: {self.owner}, Balance: {self.balance} {self.currency}"

class PremiumAccount(BankAccount):

    def deposit(self, amount):
        bonus = amount * 0.01 # 1% bonus super().deposit(amount + bonus)

    def withdraw(self, amount):
        if amount <= self.balance + 1000: # Overdraft limit
         self.balance -= amount
         self.transaction_history.append(f'Withdrew: {amount} {self.currency}')
         else:
            print("Overdraft limit exceeded!")

    def transfer(self, amount, other_account):
        commission = amount * 0.005 # 0.5% fee total_amount = amount + commission
            if total_amount <= self.balance:
                self.withdraw(total_amount) other_account.deposit(amount)
                self.transaction_history.append(f'Transferred: {amount} {other_account.currency} to {other_account.owner} with fee: {commission}')
                # Тестирование

account = BankAccount("John Doe", 500)
premium_account = PremiumAccount("Jane Doe", 1500) # Обычный счет

print(account.get_account_info()) # Вызов без параметров
print(account.get_account_info(detailed=True)) # Вызов с detailed=True
print(account.get_account_info(as_dict=True)) # Вызов с as_dict=True

account.deposit(200)
account.withdraw(100)

print(account.get_account_info(detailed=True)) # Премиум счет

premium_account.deposit(1000)
premium_account.withdraw(300)
premium_account.transfer(400, account)

print(premium_account.get_account_info(detailed=True))  ### Объяснение работы