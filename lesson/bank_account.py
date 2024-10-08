class BankAccount:
    def __init__(self,initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\n Account '{self.name}' created.\nBalance = Ugx{self.balance:.2f}")

    def getBalance(self):
        print(f"\n Account '{self.name}' balance = Ugx{self.balance:.2f}")
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\n Deposit of Ugx{amount:.2f} successful.\nNew balance = Ugx{self.balance:.2f}")