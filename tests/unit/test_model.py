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

def test_create_and_retrieve_account():
    """
    GIVEN an Account model
    WHEN a new Account is created and saved
    THEN check if the account can be retrieved correctly
    """
    # Create a new account
    account = Account('John Doe', '€', "Spain")
    assert account.name == 'John Doe'
    assert account.currency == '€'
    assert account.country == "Spain"
    assert account.account_number is not None
    assert account.balance == 0.0
    assert account.status == 'Active'

    # Add the account to the database
    db.session.add(account)
    db.session.commit()

    # Retrieve the account from the database
    retrieved_account = Account.query.filter_by(account_number=account.account_number).first()

    # Check if the retrieved account matches the original
    assert retrieved_account is not None
    assert retrieved_account.name == 'John Doe'
    assert retrieved_account.currency == '€'
    assert retrieved_account.country == "Spain"
    assert retrieved_account.balance == 0.0
    assert retrieved_account.status == 'Active'

    # Clean up
    with app.app_context():
        db.drop_all()


