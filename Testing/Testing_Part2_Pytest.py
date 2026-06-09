"""
Testing_Part2_Pytest.py
An introduction to unit testing using `pytest`.
Pytest is a popular third-party testing framework that is more concise than `unittest`.

Note: You need to install pytest to run this file (`pip install pytest`).
Run tests from terminal using: `pytest Testing_Part2_Pytest.py -v`
"""

import pytest

# --- Code to Test ---
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Not enough funds")
        self.balance -= amount

class InsufficientFundsError(Exception):
    pass

# --- Pytest Tests ---

# Fixtures are a powerful pytest feature to provide setup data to tests
@pytest.fixture
def empty_account():
    return BankAccount()

@pytest.fixture
def funded_account():
    return BankAccount(100)

def test_initial_balance(empty_account):
    assert empty_account.balance == 0

def test_deposit(empty_account):
    empty_account.deposit(50)
    assert empty_account.balance == 50

def test_withdraw(funded_account):
    funded_account.withdraw(40)
    assert funded_account.balance == 60

def test_deposit_negative_amount(empty_account):
    # Testing exceptions in pytest
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        empty_account.deposit(-10)

def test_withdraw_insufficient_funds(empty_account):
    with pytest.raises(InsufficientFundsError):
        empty_account.withdraw(10)

# Parametrized tests allow running the same test with different inputs
@pytest.mark.parametrize("deposit_amount, expected_balance", [
    (10, 10),
    (50, 50),
    (100, 100),
    (10.5, 10.5)
])
def test_multiple_deposits(empty_account, deposit_amount, expected_balance):
    empty_account.deposit(deposit_amount)
    assert empty_account.balance == expected_balance

if __name__ == "__main__":
    print("This file is meant to be run with the pytest CLI.")
    print("Command: pytest Testing_Part2_Pytest.py -v")
