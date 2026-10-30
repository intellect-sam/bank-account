import logging

import pytest
from bank import BankAccount, InsufficientFundsError
from bank.errors import InvalidAmountError
from bank.account import TransactionType

def test_deposit_increases_balance():
    acct = BankAccount("2333", "Samuel", 100)
    acct.deposit(50)
    assert acct.balance == 150

def test_overdraft_raises_and_keeps_balance():
    acct = BankAccount("2333", "Samuel", 100)
    with pytest.raises(InsufficientFundsError) as exc:
        acct.withdraw(500)
    assert exc.value.balance == 100
    assert acct.balance == 100

@pytest.mark.parametrize("amount", [0, -1, -100])
def test_deposit_rejects_non_positive(amount):
    acct = BankAccount("2333", "Samuel")
    with pytest.raises(Exception):
        acct.deposit(amount)


def test_failed_operations_leave_history__empty():
    """Prove that an invalid deposit and a failed withdrawal do not log into history"""

    acct = BankAccount("1000", "Ada", 100)

    with pytest.raises(InvalidAmountError):
        acct.deposit(-50)

    with pytest.raises(InsufficientFundsError):
        acct.withdraw(500)

    with pytest.raises(InvalidAmountError):
        acct.withdraw(-50)

    assert acct.history == []


def test_failed_operations_log_errors_and_warning(caplog):
    """Prove that failed operations record the correct log messages and levels"""

    acct = BankAccount("1000", "Ada", 100)

    with caplog.at_level(logging.WARNING):
        with pytest.raises(InvalidAmountError):
            acct.deposit(-50)
        with pytest.raises(InsufficientFundsError):
            acct.withdraw(500)

    assert len(caplog.records) == 2
    assert caplog.records[0].levelname == "WARNING"
    assert "-50" in caplog.text
    assert caplog.records[1].levelname == "WARNING"
    assert "500" in caplog.text

    assert acct.history == []

def test_successful_operations_are_recorded():
    acct = BankAccount("1000", "Ada", 100)
    acct.deposit(50)
    acct.withdraw(30)

    assert acct.history == [
        (TransactionType.DEPOSIT, 50),
        (TransactionType.WITHDRAWAL, 30)
    ]