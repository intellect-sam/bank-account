class BankErrors(Exception):
    """"Base class for all related bank errors."""
    pass

class InvalidAmountError(BankErrors):
    def __init__(self, amount):
        super().__init__(f"Invalid amount: {amount}")
        self.amount = amount

class InsufficientFundsError(BankErrors):
    def __init__(self, balance, amount):
        super().__init__(f"Insufficient funds: balance {balance}, attempted withdrawal {amount}")
        self.balance = balance
        self.amount = amount

