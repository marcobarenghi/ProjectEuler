#<p>The number, $197$, is called a circular prime because all rotations of the digits: $197$, $971$, and $719$, are themselves prime.</p>
#<p>There are thirteen such primes below $100$: $2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79$, and $97$.</p>
#<p>How many circular primes are there below one million?</p>
from itertools import permutations

def listPrimes(limit):
    array=[True for i in range(limit+1)]
    primes=[]
    p=2
    while(p**2<limit):
    	if(array[p]==True):
    		for i in range(p**2, limit+1,p):
    			array[i]=False
    	p+=1
    for p in range(2, limit+1):
    	if(array[p]):
    		primes.append(p)
    return primes

#we should remove all elements that contain at least an even digit -> not all its perms will be primes
#same goes for digit 5
def cleanPrimeList(list):
	i=0
	while(i<len(list)):
		if(list[i]>10):
			tmp=str(list[i])
			for j in range(len(tmp)):
				if(int(tmp[j])%2==0 or int(tmp[j])%5==0):
					list.remove(list[i])
					i-=1
					break
					
		i+=1
	return list

maxN=1000000
primes=listPrimes(maxN)
primes=cleanPrimeList(primes)

count = 0

for i in range(len(primes)):
	n=primes[i]
	count+=1
	#loop to create circular permutations
	for j in range(len(str(n))):
		n = (n%10)*10**(len(str(primes[i]))-1)+n//10
		#if any permutation is not prime
		if n not in primes:
			count -= 1
			break

#print the number of instances
print(count)