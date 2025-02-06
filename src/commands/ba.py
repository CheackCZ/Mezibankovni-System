# Class for command bank (total) amount: returns the total sum of all accounts balances
from src.controllers.bank_controller import BankController 

class BA:

    def __init__(self):
        self.bank_controller = BankController()

    def execute(self, ):
        try:
            total_amount = self.bank_controller.get_total_balance()
            return f"BA: {total_amount}"

        except Exception as e:
            return f"ER: {str(e)}"