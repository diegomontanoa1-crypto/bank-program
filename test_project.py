from project import deposit, withdraw, check_balance

def test_deposit():
    assert deposit(100, 50) == 150
    assert deposit(100, 0) == 100
    assert deposit(100, -5) == 100

def test_withdraw():
    assert withdraw(100, 30) == 70
    assert withdraw(100, 100) == 0
    assert withdraw(100, 101) == 100

def test_check_balance():
    assert check_balance(100) == "Balance: 100"
    assert check_balance(0) == "Balance: 0"

