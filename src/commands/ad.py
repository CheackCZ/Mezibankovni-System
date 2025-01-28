# Class for command account deposit: deposits given amount of money to account number
from src.controllers.account_controller import AccountController

class AD:

    def __init__(self):
        self.account_controller = AccountController()

    def execute(self, account_number, amount):
        try:
            self.account_controller.account_deposit(account_number=account_number, amount=amount)

            print(f"AD")
        except Exception as e:
            print(f"ER: {e}")