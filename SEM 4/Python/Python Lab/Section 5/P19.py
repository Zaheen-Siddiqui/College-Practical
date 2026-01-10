class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be greater than zero and not negative.")
            self.balance += amount
            print("Amount Deposited Successfully!")
        except ValueError as e:
            print(e)

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than zero and not negative.")
            if amount > self.balance:
                raise ValueError("Insufficient Balance!")
            self.balance -= amount
            print("Amount Withdrawn Successfully!")
        except ValueError as e:
            print(e)

    def show_balance(self):
        print(f"Account Balance: ₹{self.balance}")

    def show_details(self):
        print(f"Account Holder: {self.account_holder}, Balance: ₹{self.balance}")


accounts = {}

def bank_menu():
    while True:
        print("\nBank Menu:")
        print("1. New Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Show All Accounts")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            name = input("Enter Account Holder Name: ")
            accounts[name] = BankAccount(name)
            print("Account Created Successfully!")
        elif choice == 2:
            name = input("Enter Account Holder Name: ")
            if name not in accounts:
                print("Account not found!")
                continue
            try:
                amount = float(input("Enter amount to deposit: "))
                accounts[name].deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid positive number.")
        elif choice == 3:
            name = input("Enter Account Holder Name: ")
            if name not in accounts:
                print("Account not found!")
                continue
            try:
                amount = float(input("Enter amount to withdraw: "))
                accounts[name].withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid positive number.")
        elif choice == 4:
            name = input("Enter Account Holder Name: ")
            if name in accounts:
                accounts[name].show_balance()
            else:
                print("Account not found!")
        elif choice == 5:
            if not accounts:
                print("No accounts available!")
            else:
                for account in accounts.values():
                    account.show_details()
        elif choice == 6:
            print("Exiting the system.")
            break
        else:
            print("Invalid Choice!")

bank_menu()
