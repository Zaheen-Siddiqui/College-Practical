x = int (input('Enter a number'))
rev = 0
while (x != 0):
	num = x % 10
	rev = rev*10 + num
	x = int(x / 10)
print(rev)
