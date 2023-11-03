#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible with no remainder by all of the numbers from 1 to 20?

#brute force
n = 20
value = n
done = False
while(not done):
#	if value%100000==0:
#		print(value)
	for i in range(2, n+1):
		if(value%i==0):
			if(i==n):
				done = True
		else:
			value+=n
			break	
print("Result: ", value)