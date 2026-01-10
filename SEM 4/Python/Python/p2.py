t = 1
count = 0
for i in range(100):
 	k = 1
 	for j in range(100):
 		if(t%k == 0):
 			count = count + 1
 		k = k + 1 
 	if(count == 2):
 		print(t)
 	count = 0
 	t = t + 1
