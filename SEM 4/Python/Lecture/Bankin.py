class Bank:
	def __init__ (self):
		self.accounts = {}
	def create_account(self): 
		acc_no = input("Enter account number: ")
		if acc_no in self.accounts:
			print("Account number already exists.\n")
			return 
		name = input("Enter account holders name ")
		initial_deposit = float(input("Enter initial deposit amount "))
		self.accounts [acc_no] = {"name": name,"balance":initial_deposit}
		print ("\nAccount created successfuly \n")
	
	def depoisit(self):
		acc_no = input("Enter the account number")
		if acc_no in self.accounts:
			amount = float(input("\nEnter amount to deposit."))
			if amount > 0:
				self.accounts[acc_no]["balance"]+= amount
				print(f"Amount {amount} deposited successfuly")
			else:
				print("\nInvalid deposit\n")
		else:
			print("\nAccount does not exist\n")
	def withdraw_amt(self):
		acc_no = input("Enter the account number\n")
		if acc_no in self.accounts:
			amount = float(input("Enter amount to withdraw."))
			if 0 < amount <=self.accounts[acc_no]["balance"]:
				self.accounts[acc_no]["balance"] -= amount
				print(f"Amount {amount} Withdrawn successfuly")
			else:
				print("Invalid amount or insufficient balance")
		else:
			print("Account does not exist")
	
	def check_bal(self):
		acc_no = input("Enter the account number")
		if acc_no in self.accounts:
			print(f"Current Balnce: {self.accounts[acc_no]['balance']}")
		else:
			print("Account does not exist")
	
	def display_acc(self):
		if not self.accounts:
			print("No aacounts found")
		else:
			for acc_num, details in self.accounts.items():
				print(f"Account number:{acc_num}, Name: {details['name']}, Balance:{details['balance']}")

	def run(self):
		while(True):
			print("Banking System Menu \n1. Create New Account \n2. Deposit Money \n3. Withdraw Money \n4. Check Balance \n5. Display All Accounts \n6 Exit\n")
			choice = input("Enter you choice\n")
			if choice == '1':
				self.create_account()
			elif choice == '2':
				self.depoisit()
			elif choice == '3':
				self.withdraw_amt()
			elif choice == '4':
				self.check_bal()
			elif choice == '5':
				self.display_acc()
			elif choice == '6':
				print("Exiting the system")
				break
			else:
				print("Invalid Choice")
if __name__ == "__main__":
	bank = Bank()
	bank.run()
