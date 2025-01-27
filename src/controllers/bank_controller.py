from db.connection import Connection
from models.account import Account

class BankController:

    def __init__(self):
        self.db = Connection.get_session()

    
    def get_total_balance(self):
        total = self.db.query(self.db.func.sum(Account.balance)).scalar()
        return total if total else 0.0

    def get_number_of_accounts(self):
        return self.db.query(Account).count()