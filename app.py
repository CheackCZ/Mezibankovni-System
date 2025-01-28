from src.controllers.account_controller import AccountController

def main():
    controller = AccountController()

    # Create a new account
    account_number = controller.create_account()

    # Deposit money
    controller.account_deposit(account_number, 500.0)

    # Check balance
    balance = controller.account_ballance(account_number)
    print(f"Balance: {balance}")

    # Withdraw money
    controller.account_withdraw(account_number, 200.0)

    # Remove the account
    controller.remove_account(account_number)

if __name__ == "__main__":
    main()
