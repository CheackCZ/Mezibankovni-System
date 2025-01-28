# Class for command account remove: removes the account number (but only if the balance of the account is 0)
from src.controllers.account_controller import AccountController

class AR:

    def __init__(self):
        self.account_controller = AccountController()

    def execute(self, account_number):
        try:
            self.account_controller.remove_account(account_number=account_number)

            print(f"AR")
        except Exception as e:
            print(f"ER: {e}")