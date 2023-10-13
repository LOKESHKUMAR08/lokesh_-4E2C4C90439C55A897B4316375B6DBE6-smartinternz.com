class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        else:
            print("Insufficient funds. Cannot withdraw the specified amount.")

    def display_balance(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Account Balance: ${self.__account_balance}")

# Create an instance of BankAccount
my_account = BankAccount("12345", "John Doe", 1000.0)

# Test the deposit and withdrawal functionality
my_account.display_balance()
my_account.deposit(500.0)
my_account.withdraw(200.0)
my_account.withdraw(1500.0)  # Attempting to withdraw more than the balance
my_account.display_balance()
