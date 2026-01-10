v = int (input ('Enter number '))
if (v<0):
	print('Invalid input ')
else:
	fact = 1
	for i in range(1 , v+1):
		fact = fact * i
	print(fact)
