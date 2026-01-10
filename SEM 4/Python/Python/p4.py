v = int (input ('Enter first subject out of 20 '))
w = int (input ('Enterm second subject out of 20 '))
x = int (input ('Enter third subject out of 20 '))
y = int (input ('Enter fourth subject out of 20 '))
z = int (input ('Enterm fifth subject out of 20 '))
tot = v+w+x+y+z
if (tot>99):
	print('A++++++++++')
elif (tot <= 99 and tot > 95):
	print('A+')
elif (tot <= 95 and tot > 80):
	print('A')
elif (tot <= 80 and tot>70):
	print('B')
elif (tot <= 70 and tot>60):
	print('C')
elif (tot<=60 and tot>50):
	print('D')
else:
	print('F')
