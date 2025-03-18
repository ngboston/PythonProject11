import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Bank:
    def __init__(self, name, commission_rate):
        self.name = name
        self.commission_rate = commission_rate

    def get_commission_rate(self):
        return self.commission_rate

class BankAccount:
    def __init__(self, account_number, bank):
        self.account_number = account_number
        self.balance = 0
        self.bank = bank
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +{amount}")
            logging.info(f"Account {self.account_number}: Deposited {amount}")
        else:
            logging.warning("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transactions.append(f"Withdrawal: -{amount}")
                logging.info(f"Account {self.account_number}: Withdrawn {amount}")
            else:
                logging.warning("Insufficient funds.")
        else:
            logging.warning("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions

    def transfer(self, other_account, amount):
        if amount > 0 and amount <= self.balance:
            self.withdraw(amount)
            other_account.deposit(amount)
            logging.info(f"Transferred {amount} from {self.account_number} to {other_account.account_number}")
        else:
            logging.warning("Invalid transfer amount or insufficient funds.")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, bank, interest_rate):
        super().__init__(account_number, bank)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        logging.info(f"Account {self.account_number}: Applied interest {interest}")

class CreditAccount(BankAccount):
    def __init__(self, account_number, bank, credit_limit):
        super().__init__(account_number, bank)
        self.credit_limit = credit_limit

    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= -self.credit_limit:
            super().withdraw(amount)
            if self.balance < 0:
                commission = abs(self.balance) * self.bank.get_commission_rate()
                self.balance -= commission
                logging.info(f"Account {self.account_number}: Applied commission {commission}")
        else:
            logging.warning("Withdrawal exceeds credit limit.")


bank1 = Bank("ПриватБанк", 0.02)  # 2% комісія
bank2 = Bank("Ощадбанк", 0.01)  # 1% комісія

savings_account = SavingsAccount("SA123", bank1, 0.05)  # 5% річних
credit_account = CreditAccount("CA456", bank2, 1000)  # Кредитний ліміт 1000

savings_account.deposit(1000)
savings_account.apply_interest()

credit_account.deposit(500)
credit_account.withdraw(1200)

print(f"Savings Account Balance: {savings_account.get_balance()}")
print(f"Credit Account Balance: {credit_account.get_balance()}")

print(f"Savings Account Transactions: {savings_account.get_transactions()}")
print(f"Credit Account Transactions: {credit_account.get_transactions()}")

savings_account.transfer(credit_account, 200)

print(f"Savings Account Balance: {savings_account.get_balance()}")
print(f"Credit Account Balance: {credit_account.get_balance()}")