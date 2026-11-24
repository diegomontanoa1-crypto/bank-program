# Bank Program

A small bank account that runs in the terminal, written in Python. It started as my final project for CS50P, and I kept building on it after the course.

## What it does

- Check your balance, deposit money and withdraw money.
- Remembers your name, your balance and every movement between runs.
- Refuses amounts that are zero or negative, and withdrawals bigger than your balance.
- Keeps asking when you type something that isn't a number, instead of crashing.

## How to run it

```
python project.py
```

It needs no extra libraries to run. The first time, it asks for your name:

```
What's your name? Diego
Hello! Nice to meet you, Diego
=== MAIN MENU ===
1. Check Balance
2. Deposit
3. Withdraw
4. Movements
5. Exit
Option: 2
Amount to deposit: 100
New balance: 100
```

The next time you run it, it greets you by name and your balance is still there.

## Files it creates

The program saves its data next to `project.py`:

| File | What it holds |
|---|---|
| `names.txt` | the account holder's name |
| `balance.txt` | the current balance |
| `history.csv` | one row for every deposit and withdrawal |

These three are listed in `.gitignore`, so account data is never uploaded with the code. Delete them to start again with a new account.

## How the code is organised

Everything is in `project.py`.

**Talking to the user**

- `main` loads the saved data, greets the user and runs the menu loop until the user picks 5. It is the only function that asks questions.
- `get_number` shows a question and returns the whole number the user types. If the answer isn't a number, it asks again.

**The rules of the bank**

- `check_balance` takes the balance and returns the text to show.
- `deposit` takes the balance and an amount. It returns the new balance, or the same balance if the amount is zero or negative.
- `withdraw` takes the balance and an amount. It returns the new balance, or the same balance if the amount is zero, negative or more than the balance. Withdrawing the exact balance is allowed.

**Saving and loading**

- `save_balance` and `load_balance` write and read `balance.txt`.
- `save_movement` adds a row to `history.csv`, and `load_history` reads all the rows back as a list.
- `save_name` and `load_name` write and read `names.txt`.

## Design choices

**The balance is saved after every menu action, not only on exit.** If the program is closed in the middle of a session, nothing is lost.

**Only movements that really happened are recorded.** `main` remembers the balance before calling `deposit` or `withdraw` and compares it with the result. If the balance did not change, the request was refused and nothing is written to the history.

**A missing file and a damaged file are treated differently.** A missing file means a new account, so the program starts with a balance of 0, an empty history and no name. A balance file that can't be read as a number stops the program with a message. Starting again at 0 would overwrite the file and hide the problem.

**All the asking happens in `main`.** `deposit`, `withdraw` and `check_balance` only take values and return a result, which is what makes them possible to test.

## Tests

```
pip install -r requirements.txt
pytest test_project.py
```

There are three tests, for `deposit`, `withdraw` and `check_balance`. They cover normal amounts, zero, negative amounts, withdrawing the exact balance and withdrawing more than the balance. The save and load functions don't have tests yet.

## Background

The first version of this program was my final project for [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/). This [video demo](https://youtu.be/G6G5rzsrRBE) shows that original version, before saving, the history and the name were added.
