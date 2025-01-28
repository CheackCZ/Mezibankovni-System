# Class for command account create: created new account number in range 100000-999999 with bank code
from controllers.account_controller import AccountController

class AC:

    def __init__(self):
        self.account_controller = AccountController()

    def execute(self):
        self.account_controller.create_account()