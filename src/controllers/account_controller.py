from db.connection import Connection
from src.models.account import Account
from src.logger import setup_logger

class AccountController:
    """
    Handles account-related operations and ensures input validation.
    """

    def __init__(self):
        """
        Initializes the database session.
        """
        self.logger = setup_logger()
        self.logger.info("AccountController initialized.")
        

    def get_session(self):
        return Connection.get_session()


    def get_account(self, account_number, session):
        """
        Retrieves an account by its account number.

        :param account_number: The account number to retrieve.
        """
        account = session.query(Account).filter(Account.account_number == account_number).first()

        if account:
            self.logger.info(f"Returns the account: {account}")
            return account
        
        else:    
            self.logger.warning(f"Account with number {account_number} was not found.")
            return None


    def create_account(self):
        """
        Creates a new account with a zero balance and returns its account number.
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

        :param account_number: The account number to delete.
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

        :param account_number: The account number to retrieve the balance for.
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

        :param account_number: The account number to deposit the amount into.
        :param amount: The amount to deposit.
        """
        session = self.get_session()

        self.validate_account_number(account_number)
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

        :param account_number: The account number to withdraw the amount from.
        :param amount: The amount to withdraw.
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
        Validates that the account number is an integer and exists in the database.

        :param account_number: The account number to validate.
        """
        if type(account_number) != int:
            self.logger.error(f"Validation failed: Account number must be an integer. Received: {account_number}")
            raise ValueError("[!] Account number must be an integer.")
        
        account = self.get_account(account_number, session)
        if not account:
            self.logger.error(f"Validation failed: Account with number {account_number} does not exist.")
            raise ValueError(f"[!] Account with number {account_number} does not exist.")
        
        session.close()

    def validate_amount(self, amount):
        """
        Validates that the amount is a positive number (integer or float).

        :param amount: The amount to validate.
        """
        if type(amount) not in [int, float]:
            self.logger.error(f"Validation failed: Amount must be a number. Received: {amount}")
            raise ValueError("[!] Amount must be type of number.")
        
        if amount <= 0:
            self.logger.error(f"Validation failed: Amount must be a positive number. Received: {amount}")
            raise ValueError("[!] Amount must be a positive number.")