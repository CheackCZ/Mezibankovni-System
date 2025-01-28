from src.controllers.account_controller import AccountController

class App:

    def __init__(self):
        self.account_controller = AccountController()

    def create_account(self):
        return self.account_controller.create_account()
    
    def get_account(self, account_number):
        return self.account_controller.get_account(account_number)

    def remove_account(self, account_number):
        return self.account_controller.remove_account(account_number)

    def account_balance(self, account_number):
        return self.account_controller.account_balance(account_number)
    
    def account_deposit(self, account_number, amount):
        return self.account_controller.account_deposit(account_number, amount)
    
    def account_withdraw(self, account_number, amount):
        return self.account_controller.account_withdraw(account_number, amount)

if __name__ == "__main__":
    try:
        app = App()

        # account_number = app.create_account()

        account = app.get_account(10004)
        print(account)

        app.account_deposit(account.account_number, 1000)
        print(account)

        app.account_withdraw(account.account_number, "10000")
        print(account)

        # app.remove_account(10000)

    except ValueError as e:
        print(e)
    