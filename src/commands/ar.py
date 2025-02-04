# Class for command account remove: removes the account number (but only if the balance of the account is 0)
from src.controllers.account_controller import AccountController

class AR:

    def __init__(self):
        self.account_controller = AccountController()

    def execute(self, account_data):
        try:
            account_parts = account_data.split("/")
            if len(account_parts) != 2:
                return "ER: Invalid account format. Expected format: <account>/<ip>\r\n\r\n> "

            account_number, ip_address = account_parts
            account_number = int(account_number)

            self.account_controller.remove_account(account_number)

            return f"AR\r\n\r\n> "
        
        except ValueError:
            return "ER: Invalid number format. Account must be an integer.\r\n\r\n> "
        
        except Exception as e:
            return f"ER: {e}\r\n\r\n> "