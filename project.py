import csv
import sys

def main():
    balance = load_balance()
    name = load_name()
    if name == "":
        name = input("What's your name? ")
        save_name(name)
        print("Hello! Nice to meet you,", name)
    else: 
        print("Hello! Nice to see you again,", name)
    menu = """=== MAIN MENU ===
1. Check Balance
2. Deposit
3. Withdraw
4. Movements
5. Exit
Option: """
    option = get_number(menu)
    while option != 5:
        if option == 1:
            print(check_balance(balance))
        elif option == 2:
            amount = get_number("Amount to deposit: ")
            oldBalance = balance
            balance = deposit(balance, amount)
            if balance != oldBalance:
                save_movement("Deposit", amount)
        elif option == 3:
            amountToWithdraw = get_number("Amount to withdraw: ")
            oldBalance = balance
            balance = withdraw(balance, amountToWithdraw)
            if balance != oldBalance :
                save_movement("Withdraw", amountToWithdraw)
        elif option == 4:
            for movement in load_history():
                print(movement["kind"], movement["amount"])
        else:
            print("Invalid option!")
        save_balance(balance)
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


def save_balance(balance):
    with open ("balance.txt", "w") as file:
        file.write(str(balance))


def load_balance():
    try:
        with open("balance.txt") as file:
            text = file.read()
            return int(text) 
    except FileNotFoundError:
        return (0)
    except ValueError:
        sys.exit("Your balance has been HAAACKED CALL THE BANK RIGHT NOW!!!!!!!!!!!!!!!!!!!!!!!!!!")

def save_movement(kind, amount):
    with open("history.csv", "a", newline="") as file:
        writer = csv.DictWriter(file , fieldnames=["kind", "amount"])
        writer.writerow({"kind": kind, "amount": amount})

def load_history():
    movements = []
    try:
        with open("history.csv") as file:
            reader = csv.DictReader(file, fieldnames=["kind", "amount"])
            for row in reader:
                movements.append(row)
    except FileNotFoundError:
        return []
    return movements

def save_name(name):
    with open("names.txt", "w") as file:
        file.write(name)
    
def load_name():
    try:
        with open("names.txt") as file:
            text = file.read()
            return text
    except FileNotFoundError:
        return ""


if __name__ == "__main__":
    main()
