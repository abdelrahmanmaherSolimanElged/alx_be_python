class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional starting balance, default is 0."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount to the account."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw a specified amount if sufficient funds are available."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
