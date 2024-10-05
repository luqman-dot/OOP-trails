class BankAccount:
    interest_rate = 0.05  

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0.0 

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into {self.account_holder}'s account. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.account_holder}'s account. New balance: {self.balance}")
        else:
            print(f"Insufficient funds in {self.account_holder}'s account. Withdrawal of {amount} failed. Current balance: {self.balance}")

    def apply_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"Applied interest to {self.account_holder}'s account. Interest added: {interest}. New balance: {self.balance}")

    def display_account_info(self):
        print(f"Account holder: {self.account_holder}, Current Balance: {self.balance}")

account1 = BankAccount("Luqman")
account2 = BankAccount("Shadowsman")

# Luqman 
account1.deposit(100)
account1.withdraw(200) 
account1.apply_interest()
account1.display_account_info()

# Shadowsman 
account2.deposit(500)
account2.apply_interest()
account2.display_account_info()