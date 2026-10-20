from bank import BankErrors, BankAccount


account = BankAccount(account_number=3033, account_holder="sam", balance=100)

try:
    account.withdraw(500)
except BankErrors as e:
    print(e)
