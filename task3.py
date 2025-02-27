class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₱{amount}. Current balance: ₱{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw ₱{amount}. Current balance: ₱{self.balance}")
        else:
            print("Insufficient funds for withdrawal.")

    def display_balance(self):
        print(f"Account balance: ₱{self.balance}")

account = BankAccount("20394124", "John Doe", 100)
account.deposit(1000)
account.withdraw(500)
account.display_balance()
