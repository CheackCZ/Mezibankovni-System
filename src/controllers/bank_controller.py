from sqlalchemy.sql import func
from src.logger import setup_logger

from src.config import config
from db.connection import Connection
from src.models.account import Account


class BankController:

    logger = setup_logger() 
    
    def get_session(self):
        return Connection.get_session()
    

    def get_bank_code(self):
        bank_ip = config.HOST
        self.logger.info(f"Return the bank code (ip): {bank_ip}")
        return bank_ip
    
    def get_total_balance(self):
        session = self.get_session()

        total = session.query(func.sum(Account.balance)).scalar()
        self.logger.info(f"Return the total balance: {total}")

        session.close()

        return total 

    def get_number_of_accounts(self):
        session = self.get_session()

        total = session.query(Account).count()
        self.logger.info(f"Return the total number of accounts: {total}")

        session.close()

        return total