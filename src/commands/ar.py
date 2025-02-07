from src.controllers.account_controller import AccountController

class AR:
    """
    Handles the 'AR' command, which removes an account if its balance is zero.
    """

    def __init__(self):
        """
        Initializes the AR command with an instance of AccountController.
        """
        self.account_controller = AccountController()

    def execute(self, account_data):
        """
        Executes the 'AR' command to remove an account.

        :param account_data (str): A string in the format "<account>/<ip>".

        :return: "AR" if the account is successfully removed, or an error message.
        """
        try:
            account_parts = account_data.split("/")
            if len(account_parts) != 2:
                return "ER Invalid account format. Expected format: <account>/<ip>"

            account_number, ip_address = account_parts
            account = self.account_controller.get_account(account_number, self.account_controller.get_session())

            if account.balance != 0:
                return f"ER Cannot remove account {account_number}. Balance must be zero."

            self.account_controller.remove_account(int(account_number))

            return f"AR"
        
        except ValueError as ve: 
            return f"ER {ve}"
        
        except Exception as e:
            return f"ER: {e}"