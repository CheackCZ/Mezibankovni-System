from src.controllers.bank_controller import BankController

class BN:
    """
    Handles the 'BN' command, which retrieves the total number of accounts in the bank.
    """

    def __init__(self):
        """
        Initializes the BN command with an instance of BankController.
        """
        self.bank_controller = BankController()

    def execute(self):
        """
        Executes the 'BN' command to fetch the total number of accounts.

        :return: The total number of accounts in the format "BN: <total_accounts>" or an error message.
        """
        try:
            total_accounts = self.bank_controller.get_number_of_accounts()
            return f"BN: {total_accounts}"
        except Exception as e:
            return f"ER: {str(e)}"