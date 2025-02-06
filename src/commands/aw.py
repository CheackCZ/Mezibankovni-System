# Class for command account withdrawal: withdraws given amount of money from account number
from src.controllers.account_controller import AccountController

class AW:

    def __init__(self):
        self.account_controller = AccountController()

    def execute(self, account_data, amount):
        try:
            account_parts = account_data.split("/")
            if len(account_parts) != 2:
                return "ER: Invalid account format. Expected format: <account>/<ip>"

            account_number, ip_address = account_parts
            account_number = int(account_number)
            amount = float(amount)

            self.account_controller.account_withdraw(account_number, amount)

            return f"AW"
        
        except ValueError:
            return "ER: Invalid number format. Account must be an integer, amount must be a float."
        
        except Exception as e:
            return f"ER: {e}"