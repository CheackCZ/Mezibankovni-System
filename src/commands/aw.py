# Class for command account withdrawal: withdraws given amount of money from account number
from src.controllers.account_controller import AccountController

class AW:

    def __init__(self):
        self.account_controller = AccountController()

    def execute(self, account_number, amount):
        try:
            account_number = int(account_number)
            amount = float(amount)

            self.account_controller.account_withdraw(account_number, amount)

            return f"AW\r\n\r\n> "
        except Exception as e:
            return f"ER: {e}\r\n\r\n> "