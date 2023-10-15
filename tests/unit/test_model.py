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

def test_update_account():
    """
    GIVEN an existing Account model
    WHEN an Account is updated
    THEN check that the updated fields are saved correctly
    """
    # Create a new Account
    original_name = 'John Doe'
    updated_name = 'Jane Smith'
    original_currency = '€'
    updated_currency = '$'
    original_country = 'Spain'
    updated_country = 'USA'

    account = Account(original_name, original_currency, original_country)
    db.session.add(account)
    db.session.commit()

    # Update the Account
    account.name = updated_name
    account.currency = updated_currency
    account.country = updated_country
    db.session.commit()

    # Retrieve the updated Account
    updated_account = Account.query.get(account.id)

    # Check that the updated fields match the changes
    assert updated_account.name == updated_name
    assert updated_account.currency == updated_currency
    assert updated_account.country == updated_country

    # Clean up the database
    db.session.delete(updated_account)
    db.session.commit()
