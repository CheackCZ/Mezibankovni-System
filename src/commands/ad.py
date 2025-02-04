# Class for command account deposit: deposits given amount of money to account number
from src.controllers.account_controller import AccountController

class AD:

    def __init__(self):
        self.account_controller = AccountController()

    def execute(self, account_data, amount):
        try:
            account_parts = account_data.split("/")
            if len(account_parts) != 2:
                return "ER: Invalid account format. Expected format: <account>/<ip>\r\n\r\n> "

            account_number, ip_address = account_parts
            account_number = int(account_number)  
            amount = float(amount) 

            self.account_controller.account_deposit(account_number, amount)

            return f"AD\r\n\r\n> "
        
        except ValueError:
            return "ER: Invalid number value. Account must be an integer, amount must be a float.\r\n\r\n> "
        
        except Exception as e:
            return f"ER: {e}\r\n\r\n> "