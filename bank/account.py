from .errors import InsufficientFundsError, InvalidAmountError


class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(f"Insert a valid amount, it cant be {amount}")

        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        