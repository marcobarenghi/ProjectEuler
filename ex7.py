#By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, we can see that the $6$th prime is $13$.
#What is the $10\,001$st prime number?
primes=[2]
n=3
desiredNPrime=10001

while(len(primes) < desiredNPrime ):
	print(len(primes))
	count = 0
	#do not need to divide by 2
	for i in range(3,int(n/2)+2):
		if(n%i>0):
			count+=1
		else:
			break
	if count== len(range(3,int(n/2)+2)):
			primes.append(n)
	n+=2
			
print(primes)
