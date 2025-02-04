# Class for command account deposit: deposits given amount of money to account number
from src.controllers.account_controller import AccountController

class AD:

    def __init__(self):
        self.account_controller = AccountController()

    def execute(self, account_number, amount):
        try:
            account_number = int(account_number)
            amount = float(amount)

            self.account_controller.account_deposit(account_number, amount)

            return f"AD\r\n\r\n> "
        except Exception as e:
            return f"ER: {e}\r\n\r\n> "