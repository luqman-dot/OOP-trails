class BankAccount:
    interest_rate = 0.05    #class attribute rep the interest rate for all accounts

    def __init__(self, account_holder):    #initialize the accounts
        self.account_holder = account_holder
        self.balance = 0.0 

    def deposit(self, amount):  #func to add the specified amount to the balance and display the updated balance
        self.balance += amount
        print(f"Deposited {amount} into {self.account_holder}'s account. New balance: {self.balance}")

    def withdraw(self, amount):  #check if bank balance is sufficient
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.account_holder}'s account. New balance: {self.balance}")
        else:
            print(f"Insufficient funds in {self.account_holder}'s account. Withdrawal of {amount} failed. Current balance: {self.balance}")

    def apply_interest(self):   #calc  the interest based on the balance 
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"Applied interest to {self.account_holder}'s account. Interest added: {interest}. New balance: {self.balance}")

    def display_account_info(self):
        print(f"Account holder: {self.account_holder}, Current Balance: {self.balance}")

account1 = BankAccount("Luqman")  #BankAccount objects for different account holders
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