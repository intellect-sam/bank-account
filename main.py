from bank import BankErrors, BankAccount
from pathlib import Path
from bank.storage import save_accounts, load_accounts, find_account

account = BankAccount(account_number="3033", account_holder="sam", balance=100)

try:
    account.withdraw(50)
except BankErrors as e:
    print(e)
