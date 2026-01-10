listjhb = []
bool = True
while (bool):
	print ("Enter \n1 for adding number \n2 end\n ")
	ch =  int (input ("Enter thy choice"))
	
	if(ch == 1):
		ele =  int(input("Enter thy element"))
		listjhb.append(ele)
		print (listjhb)
	
	else:
		bool = False

print("Sum of list",sum(listjhb))
print("Average of list",sum(listjhb)/len(listjhb))
rev =listjhb[::-1]
print("Reverse of list",rev)
