"""Bank Account (Simple)
Create a class BankAccount with attributes: name, balance.

Methods: deposit(amount), withdraw(amount), check_balance().

Create one object and perform deposit, withdraw, and check balance using user input."""
class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print("deposited amount:",self.balance)
    def withdraw(self,amount):
        self.balance -= amount
        print("withdrawn amount:",self.balance)
    def check_balance(self):
        if self.balance < 0:
            print("You don't have enough money!")
        else:
            print("balance is:", self.balance)
b = BankAccount("John", 22)
b.deposit(100)
b.withdraw(100)
b.check_balance()



