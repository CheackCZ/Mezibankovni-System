# Class for command account remove: removes the account number (but only if the balance of the account is 0)
from src.controllers.account_controller import AccountController

class AR:

    def __init__(self):
        self.account_controller = AccountController()

    def execute(self, account_number):
        try:
            account_number = int(account_number)
            self.account_controller.remove_account(account_number)

            return f"AR\r\n\r\n> "
        except Exception as e:
            return f"ER: {e}\r\n\r\n> "