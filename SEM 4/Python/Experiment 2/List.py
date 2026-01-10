list_ = []
bool = True
while (bool):
	print ("Enter \n1 for append \n2 for insert at position \n3 for index of element \n4 for remove element \n5 for pop element \n6 for clear list \n7 for count of elements \n8 for reverse \n9 for length of list \n10 for sort \n11 for exit \n ")
	ch =  int (input ("Enter thy choice"))
	
	if(ch == 1):
		ele =  int(input("Enter thy element"))
		list_.append(ele)
		print (list_)
	
	elif(ch == 2):
		ele =  int(input("Enter thy element"))
		pos =  int(input("Enter thy position"))
		list_.insert(pos,ele)
		print (list_)
	
	elif(ch == 3):
		ele =  int(input("Enter the element of which thy wish to find the position of"))
		print ("position of element",list_.index(ele))
	
	elif(ch == 4):
		ele =  int(input("Enter the element to remove"))
		list_.remove(ele)
		print (list_)
	
	elif(ch == 5):
		ele =  int(input("Enter the element to pop"))
		print ("popped out element",list_.pop(ele))
	
	elif(ch == 6):
		list_.clear(ele)
		print ("list is empty")
	
	elif(ch == 7):
		print ("Count of element",list_.count(ele))
	
	elif(ch == 8):
		rev =list_[::-1]
		print ("reverse of list",rev)
		
	elif(ch == 9):
		print ("length of list",len(list_))
	
	elif(ch == 10):
		print ("Sorted list",list_.sort())
	elif(ch == 11):
		bool = false
	
	else:
		print("Invalid Input")
	
	
	
	
