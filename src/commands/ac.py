from src.controllers.account_controller import AccountController

class AC:
    """
    Handles the 'AC' command, which creates a new account in the system.
    """

    def __init__(self):
        """
        Initializes the AC command with an instance of AccountController.
        """
        self.account_controller = AccountController()

    def execute(self):
        """
        Executes the 'AC' command to create a new account.

        :return: The newly created account number in the format "AC: <account_number>" or an error message.
        """
        try:
            account_number = self.account_controller.create_account()

            return f"AC: {account_number}"
        
        except Exception as e:
            return f"ER {e}"