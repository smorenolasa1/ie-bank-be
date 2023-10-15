from iebank_api.models import Account
import pytest
from iebank_api import db, app

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
    db.session.add(account)
    db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client

    with app.app_context():
        db.drop_all()

def test_account_check():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the __repr__ method is defined correctly
    """
    account = Account("John Doe", "Spain", "€")
    assert repr(account) == f"<Event '{(account.account_number)}'>"

 
