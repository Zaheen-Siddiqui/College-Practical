def Balance():
	Bal = 10000
	if(Bal <= 0):
		print("\nEntered value must not  be 0 or negative \n \n")
		return
	print(f"Current balance is {Bal}")
	return Bal
def Deposit(Bal, Dep):
	print(f"Old balance is {Bal}")
	Bal += Dep
	print(f"New balance is {Bal}")
def Withdraw(Bal, With):
	print(f"Old balance is {Bal}")
	if (With < Bal):
		Bal -= With
		print(f"New balance is {Bal}")
	else:
		print("Insufficient balance")
def Exit():
	return False

Bal = Balance()
WhileCond = True
while(WhileCond):
	choice = int(input("Please enter \n1 for making a deposit \n2 for makin a withdrawal \n3 for exiting the procedure "))
	if(choice == 1):
		Dep = int(input("Please enter the amount to be deposited "))
		if(Dep <= 0):
			print("\nEntered value must not  be 0 or negative \n \n ")
			continue
		Deposit(Bal,Dep)
	elif(choice == 2):
		With = int(input("Please enter the amount to be withdrawn "))
		if(With <= 0):
			print("\nEntered value must not  be 0 or negative \n \n")
			continue
		Withdraw(Bal, With)
	elif(choice == 3):
		WhileCond = Exit()
	else:
		print("Incorrect choice. \nPlease Try again ")
