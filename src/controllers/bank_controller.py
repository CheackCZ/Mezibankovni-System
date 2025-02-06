from sqlalchemy.sql import func
from src.logger import setup_logger

from src.config import config
from db.connection import Connection
from src.models.account import Account


class BankController:
    """
    Handles operations related to the bank, including retrieving total balance,
    number of accounts, and bank code.
    """

    logger = setup_logger() 
    
    def get_session(self):
        """
        Retrieves a new database session.

        :return: A new SQLAlchemy session.
        """
        return Connection.get_session()
    

    def get_bank_code(self):
        """
        Retrieves the bank code, which is represented by the server's IP address.

        :return: The bank's IP address as a string.
        """
        bank_ip = config.HOST
        self.logger.info(f"Return the bank code (ip): {bank_ip}")
        return bank_ip
    
    def get_total_balance(self):
        """
        Calculates the total balance of all accounts in the system.

        :return: The sum of all account balances as a float.
        """
        session = self.get_session()

        total = session.query(func.sum(Account.balance)).scalar()
        self.logger.info(f"Return the total balance: {total}")

        session.close()

        return total 

    def get_number_of_accounts(self):
        """
        Retrieves the total number of accounts in the system.

        :return: The total count of accounts as an integer.
        """
        session = self.get_session()

        total = session.query(Account).count()
        self.logger.info(f"Return the total number of accounts: {total}")

        session.close()

        return total