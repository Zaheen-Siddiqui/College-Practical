l1 = []
l2 = []
def CreateList():
	n = int(input("Enter the number of elements in the first list "))
	for i in range (n):
		ele=int(input("\nEnter the element "))
		l1.append(ele)
	n = int(input("Enter the number of elements in the second list "))
	for i in range (n):
		ele=int(input("\nEnter the element "))
		l2.append(ele)
	
def MergeList():
	for i in range(len(l2)):
		l1.append(l2[i])

CreateList() 
print(f"\nFirst list: {l1} \nSecond list: {l2}")
MergeList()
print(f"\nMerged list: {l1}")
