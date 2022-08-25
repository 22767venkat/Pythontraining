def withdraw(self, balance, amount):
    if (balance < amount):
        raise insufficientbal("InSufficientBalanace")
    balance = balance - amount