from src.controllers.bank_controller import BankController 

class BA:
    """
    Handles the 'BA' command, which retrieves the total sum of all account balances.
    """

    def __init__(self):
        """
        Initializes the BA command with an instance of BankController.
        """
        self.bank_controller = BankController()

    def execute(self, ):
        """
        Executes the 'BA' command to fetch the total balance of all accounts.

        :return: The total sum of all account balances in the format "BA: <total_amount>" or an error message.
        """
        try:
            total_amount = self.bank_controller.get_total_balance()
            return f"BA: {total_amount}"

        except Exception as e:
            return f"ER: {str(e)}"