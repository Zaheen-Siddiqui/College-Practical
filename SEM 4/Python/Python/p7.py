x = int (input('Enter a number'))
sum = 0
while (x != 0):
	num = x % 10
	sum = sum + num
	x = int(x / 10)
print(sum)
