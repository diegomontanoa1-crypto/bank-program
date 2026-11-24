# Bank program
#### Video Demo: https://youtu.be/G6G5rzsrRBE
#### Description:

Bank program is a really basic concept of how a program for a bank could work, you can check your balance, withdraw or deposit money and it runs in a loop until someone presses "4" to exit.

## How to run it

```
python project.py
```

## Files

- project.py
- test_project.py
- requirements.txt
- README.md

### project.py

**`main`**: Main creates a balance starting at 0 and prints out the menu, it then has an if, elif and else to match the menu's number so that then the functions get called inside of a loop so that it only exits if the user presses "4".

**`get_number`**: It takes a "prompt" which is text and then returns the integer the user typed as an answer. If the user did not type a number, it prints a message asking again until it's an int. It is used for the deposit amount, withdraw amount and for the menu option.

**`check_balance`**: It takes the current balance and returns a text with the balance, and it does not print anything because main prints what it returned.

**`deposit`**: It takes the current balance and the amount to deposit, if the amount is above 0, it adds it and returns the new balance. If the amount is 0 or negative it prints out "invalid amount" and returns the balance unchanged.

**`withdraw`**: It takes the current balance and amount to withdraw, to then check if the amount is 0 or negative and prints "invalid amount" to then return the balance unchanged. If the amount is bigger than the current balance it prints "Not enough balance" and returns the balance unchanged. Otherwise it subtracts it and returns the new balance. And withdrawing the exact balance is allowed to leave 0 in the account.

### test_project.py

It has 3 tests, one per function.

- For deposit it tests a normal amount, zero and a negative amount.
- For withdraw it tests a normal amount, the exact balance and one more than the balance. Eg: balance 100, test 101.
- For check balance it tests the text for a balance of 100 and 0.

It runs with:

```
pytest test_project.py
```

### requirements.txt

It lists the only requirement which is: pytest

## Design choices

I decided to have a function for withdraw, deposit, check balance so that I could simply call it in main based on the option the user typed. Also there is a function for getting a number so that I don't repeat code that I need in three different places, and also since the while True is inside get_number it means that if someone types "Cat" the program asks for it again, instead of just crashing, the function only returns once it has a real number in it. That way main is as organized as possible, it does not have any math on it but just calls the functions.

I had to move asking into main instead of including it on the functions so that I could test it correctly, because if not it just asked me for a value instead of responding it. And for check balance I made it return the text.
