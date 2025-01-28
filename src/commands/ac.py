# Class for command account create: created new account number in range 100000-999999 with bank code
from src.controllers.account_controller import AccountController

class AC:

    def __init__(self):
        self.account_controller = AccountController()

    def execute(self):
        try:
            account_number = self.account_controller.create_account()

            print(f"AC: {account_number}")
        except Exception as e:
            print(f"ER: {e}")