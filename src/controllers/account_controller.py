from src.logger import setup_logger

from db.connection import Connection
from src.models.account import Account

class AccountController:
    """
    Handles account-related operations and ensures input validation.
    """

    logger = setup_logger()

    def get_session(self):
        """
        Retrieves a new database session.

        :return: A new SQLAlchemy session.
        """
        return Connection.get_session()


    def get_account(self, account_number, session):
        """
        Retrieves an account by its account number.

        :param account_number (int): The account number to retrieve.
        :param session: The SQLAlchemy session to use for the query.

        :return: The account object if found, else None.
        """
        account = session.query(Account).filter(Account.account_number == account_number).first()

        if not account:        
            self.logger.warning(f"Account with number {account_number} was not found.")
            return None
        
        return account


    def create_account(self):
        """
        Creates a new account with a zero balance.

        :return: The newly created account's account number.
        """
        session = self.get_session()

        new_account = Account(balance=0.0)
    
        session.add(new_account)
        session.commit()
        session.refresh(new_account)

        session.close()
    
        self.logger.info(f"New account created: {new_account.account_number} with balance {new_account.balance}.")
        return new_account.account_number
    

    def remove_account(self, account_number):
        """
        Deletes an account by its account number after validation.

        :param account_number (int): The account number to delete.
        """
        session = self.get_session()

        self.validate_account_number(account_number, session)
        
        account = self.get_account(account_number, session)
        
        if account:
            session.delete(account)
            session.commit()
            self.logger.info(f"Account {account_number} has been removed.")

        session.close()


    def account_ballance(self, account_number):
        """
        Retrieves the balance of an account.

        :param account_number (int): The account number to retrieve the balance for.

        :return: The current balance of the account.
        """
        session = self.get_session()

        self.validate_account_number(account_number, session)
        
        account = self.get_account(account_number, session)
        self.logger.info(f"Retrieved balance for account {account_number}: {account.balance}.")

        session.close()

        return account.balance  


    def account_deposit(self, account_number, amount):
        """
        Deposits a specified amount into an account after validation.

        :param account_number (int): The account number to deposit the amount into.
        :param amount (float): The amount to deposit.
        """
        session = self.get_session()

        self.validate_account_number(account_number, session)
        self.validate_amount(amount)

        account = self.get_account(account_number, session)
        if account:
            account.balance += amount
            session.commit()
            session.refresh(account)

            self.logger.info(f"Deposited {amount} to account {account_number}. New balance: {account.balance}.")
        
        session.close()


    def account_withdraw(self, account_number, amount):
        """
        Withdraws a specified amount from an account after validation and ensures sufficient balance.

        :param account_number (int): The account number to withdraw the amount from.
        :param amount (float): The amount to withdraw.
        """
        session = self.get_session()

        self.validate_account_number(account_number, session)
        self.validate_amount(amount)
       
        account = self.get_account(account_number, session)

        if account and account.balance >= amount:
            account.balance -= amount

            session.commit()
            session.refresh(account)
            
            self.logger.info(f"Withdrew {amount} from account {account_number}. New balance: {account.balance}.")
        
        else:
            self.logger.error(f"Withdrawal of {amount} from account {account_number} failed. Insufficient balance.")
            raise ValueError("[!] Don't have enough money on the account balance")
        
        session.close()


    
    def validate_account_number(self, account_number, session):
        """
        Validates that the account number is an integer, within the valid range, and exists in the database.

        :param account_number (int): The account number to validate.
        :param session: The SQLAlchemy session to use for validation.
        """
        if type(account_number) != int:
            self.logger.error(f"Validation failed: Account number must be an integer. Received: {account_number}")
            raise ValueError("[!] Account number must be an integer.")

        if not 10000 <= account_number <= 99999:
            self.logger.error(f"Invalid account number: {account_number}")
            raise ValueError("[!] Account number must be between 10000 and 99999.")

        account = self.get_account(account_number, session)
        if not account:
            self.logger.error(f"Validation failed: Account with number {account_number} does not exist.")
            raise ValueError(f"[!] Account with number {account_number} does not exist.")
        
        session.close()

    def validate_amount(self, amount):
        """
        Validates that the amount is a positive number (integer or float).

        :param amount (float): The amount to validate.
        """
        if type(amount) not in [int, float]:
            self.logger.error(f"Validation failed: Amount must be a number. Received: {amount}")
            raise ValueError("[!] Amount must be type of number.")
        
        if amount <= 0:
            self.logger.error(f"Validation failed: Amount must be a positive number. Received: {amount}")
            raise ValueError("[!] Amount must be a positive number.")