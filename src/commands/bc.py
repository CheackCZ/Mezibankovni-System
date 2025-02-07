import os

from src.controllers.bank_controller import BankController

class BC:
    """
    Handles the 'BC' command, which retrieves the bank code (IP address).
    """

    def __init__(self):
        """
        Initializes the BC command with an instance of BankController.
        """
        self.bank_controller = BankController()


    def execute(self):
        """
        Executes the 'BC' command to fetch the bank code.

        :return: The bank code (IP address) in the format "BC <bank_ip>" or an error message.
        """
        try:
            bank_ip = self.bank_controller.get_bank_code()
            return f"BC {bank_ip}"
        
        except Exception as e:
            return f"ER {e}"