from iebank_api.models import Account
import pytest

def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    account = Account('John Doe', '€', "Spain")
    assert account.name == 'John Doe'
    assert account.currency == '€'
    assert account.country == "Spain"
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == 'Active'

def test_account_deposit():
    account = Account(name="John Doe", currency="€", country="Spain")
    initial_balance = account.balance
    deposit_amount = 100
    account.deposit(deposit_amount)
    assert account.balance == initial_balance + deposit_amount

def test_account_withdraw():
    account = Account(name="John Doe", currency="€", country="Spain")
    account.balance = 200  # Set an initial balance
    withdrawal_amount = 100
    account.withdraw(withdrawal_amount)
    assert account.balance == 100  # The new balance after withdrawal    