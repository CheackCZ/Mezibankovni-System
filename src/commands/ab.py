from src.controllers.account_controller import AccountController

class AB:
    """
    Handles the 'AB' command, which retrieves the balance of a given account.
    """

    def __init__(self):
        """
        Initializes the AB command with an instance of AccountController.
        """
        self.account_controller = AccountController()

    def execute(self, account_data):
        """
        Executes the 'AB' command to fetch the account balance.

        :param account_data (str): A string in the format "<account>/<ip>".

        :return: The account balance in the format "AB <balance>" or an error message.
        """
        try:
            account_parts = account_data.split("/")
            if len(account_parts) != 2:
                return "ER: Invalid account format. Expected format: <account>/<ip>"

            account_number, ip_address = account_parts
            account_number = int(account_number)

            balance = self.account_controller.account_ballance(account_number)

            return f"AB {balance}"
       
        except ValueError:
            return "ER: Invalid number format. Account must be an integer."
        
        except Exception as e:
            return f"ER: {e}"
