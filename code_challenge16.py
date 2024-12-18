name= input("Enter your name-->  ")
# BankAccount class
class BankAccount:
    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit

    # Function to deposit amount
    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        if amount > 0:
            self.balance += amount
            print("\nAmount Deposited: ₱", amount)
            print("Current Balance: ₱", self.balance)
        else:
            print("Deposit amount must be positive.")
            
# Function to withdraw the amount
def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

# Function to display the amount
def display(self):
        print("\n Net Available Balance =", self.balance)




# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
 
# Driver code
  
# creating an object of class
s = Bank_Account()
  
# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()