from src.controllers.account_controller import AccountController
from src.p2p.proxy import Proxy
from src.config import config

class AW(Proxy):
    """
    Handles the 'AW' command, which withdraws a specified amount from an account.
    """

    def __init__(self):
        """
        Initializes the AW command with an instance of AccountController.
        """
        self.account_controller = AccountController()

    def execute(self, account_data, amount):
        """
        Executes the 'AW' command to withdraw an amount from a specified account.

        :param account_data (str): A string in the format "<account>/<ip>".
        :param amount (float): The amount to withdraw.

        :return: "AW" if the withdrawal is successful, or an error message.
        """
        try:
            account_parts = account_data.split("/")
            if len(account_parts) != 2:
                return "ER Invalid account format. Expected format: <account>/<ip>"

            account_number, ip_address = account_parts

            if ip_address != config.HOST:
                return Proxy.proxy_request("AW", [account_data, amount], ip_address)

            self.account_controller.account_withdraw(int(account_number), float(amount))

            return f"AW"
        
        except ValueError as ve:
            return f"ER {ve}"
        
        except Exception as e:
            return f"ER {e}"