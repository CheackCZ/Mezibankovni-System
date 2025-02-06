# Class for command bank number of clients: returns the number of clients in the bank
from src.controllers.bank_controller import BankController

class BN:

    def __init__(self):
        self.bank_controller = BankController()

    def execute(self):
        try:
            total_accounts = self.bank_controller.get_number_of_accounts()
            return f"BN: {total_accounts}"
        except Exception as e:
            return f"ER: {str(e)}"