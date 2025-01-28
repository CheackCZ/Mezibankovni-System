# Class for command account withdrawal: withdraws given amount of money from account number
from src.controllers.account_controller import AccountController

class AW:

    def __init__(self):
        self.account_controller = AccountController()

    def execute(self, account_number, amount):
        try:
            self.account_controller.account_withdraw(account_number=account_number, amount=amount)

            print(f"AW")
        except Exception as e:
            print(f"ER: {e}")