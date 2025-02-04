# Class for command account create: created new account number in range 100000-999999 with bank code
from src.controllers.account_controller import AccountController

class AC:

    def __init__(self):
        self.account_controller = AccountController()

    def execute(self):
        try:
            account_number = self.account_controller.create_account()

            return f"AC: {account_number}\r\n\r\n> "
        except Exception as e:
            return f"ER: {e}\r\n\r\n> "