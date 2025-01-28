from db.connection import Connection
from models.account import Account
from src.logger import setup_logger 

class BankController:

    def __init__(self):
        self.db = Connection.get_session()

        self.logger = setup_logger()

    
    def get_total_balance(self):
        total = self.db.query(self.db.func.sum(Account.balance)).scalar()
        self.logger.info(f"Return the total balance: {total}")
        return total if total else 0.0

    def get_number_of_accounts(self):
        total = self.db.query(Account).count()
        self.logger.info(f"Return the total number of accounts: {total}")
        return total if total else 0.0