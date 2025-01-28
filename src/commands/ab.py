# Class for command account balance: returns balance for given account_number
from src.controllers.account_controller import AccountController

class AB:

    def __init__(self):
        self.account_controller = AccountController()

    def execute(self, account_number):
        try:
            balance = self.account_controller.account_ballance(account_number=account_number)

            print(f"AB: {balance}")
        except Exception as e:
            print(f"ER: {e}")
