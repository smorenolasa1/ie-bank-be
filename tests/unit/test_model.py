from iebank_api.models import Account
import pytest
from iebank_api import db, app

class Account(db.Model):
    __tablename__ = 'accounts'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    currency = db.Column(db.String(3), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    account_number = db.Column(db.String(16), nullable=False, unique=True)
    balance = db.Column(db.Float, default=0.0)
    status = db.Column(db.String(16), default='Active')

    def __init__(self, name, currency, country):
        self.name = name
        self.currency = currency
        self.country = country
        # Generate an account number and set other default values.

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

    def test_account_deposit():
        account = Account('John Doe', '€', "Spain")
        initial_balance = account.balance
        deposit_amount = 100
        account.deposit(deposit_amount)
        assert account.balance == initial_balance + deposit_amount

    def test_account_withdraw():
        account = Account(name="John Doe", currency="€", country="Spain")
        account.balance = 200  
        withdrawal_amount = 100
        account.withdraw(withdrawal_amount)
        assert account.balance == 100    






