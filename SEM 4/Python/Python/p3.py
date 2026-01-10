x = int (input('Enter first number'))
y = int (input('Enter second number'))
z = int (input('Enterm third number'))
if (x < y):
	smallest = x
	largest = y
else:
	smallest = y
	largest = x
if (z < smallest):
	smallest = z
if (z > largest):
	largest = z
print ('Smallest number is' ,smallest)
print ('Largest number is' ,largest)
