from dataclasses import dataclass, field
from datetime import datetime
import logging
from .errors import InsufficientFundsError, InvalidAmountError
from enum import Enum

logger = logging.getLogger(__name__)

class TransactionType(Enum):
    WITHDRAWAL = "withdraw"
    DEPOSIT = "deposit"

@dataclass
class BankAccount:
    account_number: str
    account_holder: str
    balance: int = 0
    tags: list[str] = field(default_factory=list)
    history: list[tuple[TransactionType, int]] = field(default_factory=list)

    def deposit(self, amount: int) -> None:
        if amount <= 0:
            msg = f"Failed Deposit: Amount ₦{amount} must be positive"
            logger.warning(msg)
            raise InvalidAmountError(msg)
        self.balance += amount
        self.history.append((TransactionType.DEPOSIT, amount))
        logger.info("Amount %s successfully deposited ₦%s | with balance of ₦%s", self.account_number, amount, self.balance)

    def withdraw(self, amount: int) -> None:
        if amount <= 0:
            msg = f"Failed to withdraw: Amount {amount} must greater than 0" 
            logger.warning(msg)
            raise InvalidAmountError(msg)

        if amount > self.balance:
            msg = f"Failed withdrawal: Account {self.account_number} attempted to withdraw ₦{amount} but only has ₦{self.balance}."
            logger.warning(msg)
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        self.history.append((TransactionType.WITHDRAWAL, amount))
        logger.info(f"Account {self.account_number}: Successfully withdrew ₦{amount}. New balance: ₦{self.balance}.")
