# Class for command account balance: returns balance for given account_number
from src.controllers.account_controller import AccountController

class AB:

    def __init__(self):
        self.account_controller = AccountController()

    def execute(self, account_number):
        try:
            account_number = int(account_number)
            balance = self.account_controller.account_ballance(account_number)

            return f"AB: {balance}\r\n\r\n> "
        except Exception as e:
            return f"ER: {e}\r\n\r\n> "
