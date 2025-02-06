# Class for command bank code: returns the bank code
import os

from src.controllers.bank_controller import BankController

class BC:
    """
    Class for handling bank code requests.
    """

    def __init__(self):
        self.bank_controller = BankController()


    def execute(self):
        try:
            bank_ip = self.bank_controller.get_bank_code()
            return f"BC {bank_ip}"
        
        except Exception as e:
            return f"ER: {e}"