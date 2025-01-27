from db.connection import Connection
from models.account import Account

class AccountController:

    def __init__(self):
        self.db = Connection.get_session()


    def create_account(self):
        new_account = Account(balance=0.0)
    
        self.db.add(new_account)
        self.db.commit()
        self.db.refresh(new_account)
    
        return new_account.account_number
    

    def remove_account(self, account_number):
        account = self.db.query(Account).filter(Account.account_number == account_number).first()
        self.db.delete(account)
        self.db.commit()


    def account_ballance(self, account_number):
        account = self.db.query(Account).filter(Account.account_number == account_number).first()
        return account.balance


    def account_deposit(self, account_number, amount):
        account = self.db.query(Account).filter(Account.account_number == account_number).first()
        account.balance += amount

    def account_withdraw(self, account_number, amount):
        account = self.db.query(Account).filter(Account.account_number == account_number).first()
        account.balance -= amount