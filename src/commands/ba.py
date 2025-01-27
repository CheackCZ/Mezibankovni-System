# Class for command bank (total) amount: returns the total sum of all accounts balances

# Class for command account balance: returns the balance of account number
from controllers.bank_controller import BankController 

class BA:

    def __init__(self):
        self.bank_controller = BankController()

    def execute(self, account_number):
        try:
            total_amount = self.bank_controller.get_total_balance(account_number)
            return f"BA: {total_amount}"
        except Exception as e:
            return f"ER: {str(e)}"