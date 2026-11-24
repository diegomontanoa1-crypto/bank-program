def main():
    balance = 0
    menu = """=== MAIN MENU ===
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Option: """
    option = get_number(menu)
    while option != 4:
        if option == 1:
            print(check_balance(balance))
        elif option == 2:
            amount = get_number("Amount to deposit: ")
            balance = deposit(balance, amount)
        elif option == 3:
            amountToWithdraw = get_number("Amount to withdraw: ")
            balance = withdraw(balance, amountToWithdraw)
        else:
            print("Invalid option!")
        option = get_number(menu)
    print("Goodbye!")

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please type a number.")

def check_balance(currentBalance):
    return(f"Balance: {currentBalance}")

def deposit(currentBalance, amount):
    if amount > 0:
        currentBalance = currentBalance + amount
        print("New balance:", currentBalance)
    else:
        print("Invalid amount")
    return currentBalance

def withdraw(currentBalance, amountToWithdraw):
    if amountToWithdraw <= 0:
        print("Invalid amount")
    elif amountToWithdraw > currentBalance:
        print("Not enough balance to withdraw. Current balance:", currentBalance)
    else:
        currentBalance = currentBalance - amountToWithdraw
        print("New balance after withdraw:", currentBalance)
    return currentBalance


if __name__ == "__main__":
    main()
