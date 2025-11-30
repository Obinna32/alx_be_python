class BankAccount:

    def __init__(self, account_balance):
        self.account_balance = 0

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount >= self.account_balance:
            print("Insufficient funds")
        else:
            self.account_balance -= amount

    def display_balance(self):
        print(f" Current Balance ${self.account_balance}")

