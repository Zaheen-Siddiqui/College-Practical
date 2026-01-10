class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self,ammount):
        self.balance += ammount
        print(f"Deposited ${ammount}. New Balance: ${self.balance}")
    
    def withdraw(self,ammount):
        if ammount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= ammount
            print(f"Withdraw ${ammount}. Remaining Balance: ${self.balance}")
            
class SavingAccount (BankAccount):
    def __init__(self,account_holder, balance,interst_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interst_rate
    
    def add_interest (self):
        interest = self.balance * self.interest_rate/100
        self.balance += interest
        print(f"Interest added ${interest}. New Balance: ${self.balance}")
        
class CurrentAccount(BankAccount):
    def __init__(self,account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self,ammount):
        if ammount > self.balance:
            print("Insufficient Funds")
        else:
            super().withdraw

print("===Saving Account===")
savings = SavingAccount("Ajay", 5000,3)
print(f"Account Holder: {savings.account_holder}")
print(f"Interest Rate: {savings.interest_rate}")
savings.deposit(1000)
savings.withdraw(2000)
savings.add_interest()

print("\n===Current Account===")
current = CurrentAccount("Rohan", 2000,1000)
print(f"Account Holder: {current.account_holder}")
print(f"Overdraft: {current.overdraft_limit}")
current.deposit(500)
current.withdraw(3000)
current.withdraw(1000)

# Choice = int(input("Enter \n1. To create a savings account \n2. To create a current account"))
# while True:
#     if Choice = 1: