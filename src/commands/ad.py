from src.controllers.account_controller import AccountController
from src.p2p.proxy import Proxy
from src.config import config

class AD(Proxy):
    """
    Handles the 'AD' command, which deposits a specified amount into an account.
    """

    def __init__(self):
        """
        Initializes the AD command with an instance of AccountController.
        """
        self.account_controller = AccountController()

    def execute(self, account_data, amount):
        """
        Executes the 'AD' command to deposit an amount into a specified account.

        :param account_data (str): A string in the format "<account>/<ip>".
        :param amount (float): The amount to deposit.
        
        :return: "AD" if the deposit is successful, or an error message.

        """
        try:
            account_parts = account_data.split("/")
            if len(account_parts) != 2:
                return "ER Invalid account format. Expected format: <account>/<ip>"

            account_number, ip_address = account_parts

            if ip_address != config.HOST:
                return Proxy.proxy_request(command="AD", args=[account_data, amount], target_ip=ip_address)

            self.account_controller.account_deposit(int(account_number), float(amount))

            return f"AD"
        
        except ValueError as ve:
            return f"ER {ve}"
        
        except Exception as e:
            return f"ER {e}"