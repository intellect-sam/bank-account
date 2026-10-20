import pytest
from bank import BankAccount, InsufficientFundsError

def test_deposit_increases_balance():
    acct = BankAccount(2333, "Samuel", 100)
    acct.deposit(50)
    assert acct.balance == 150

def test_overdraft_raises_and_keeps_balance():
    acct = BankAccount(2333, "Samuel", 100)
    with pytest.raises(InsufficientFundsError) as exc:
        acct.withdraw(500)
    assert exc.value.balance == 100
    assert acct.balance == 100

@pytest.mark.parametrize("amount", [0, -1, -100])
def test_deposit_rejects_non_positive(amount):
    acct = BankAccount(2333, "Samuel")
    with pytest.raises(Exception):
        acct.deposit(amount)