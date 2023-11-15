#<p>The arithmetic sequence, $1487, 4817, 8147$, in which each of the terms increases by $3330$, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the $4$-digit numbers are permutations of one another.</p>
#<p>There are no arithmetic sequences made up of three $1$-, $2$-, or $3$-digit primes, exhibiting this property, but there is one other $4$-digit increasing sequence.</p>
#<p>What $12$-digit number do you form by concatenating the three terms in this sequence?</p>
def listPrimes(n):
    primes=[True]*(n+1)
    primes[0]=False
    primes[1]=False

    for i in range(2, int(n**0.5)+1):
        if(primes[i]):
            for j in range(i*i, n+1, i):
                primes[j]=False

    return [num for num, isPrime in enumerate(primes) if isPrime]

def isPrime(n):
    if(n==2):
        return True
    else:
        for i in range(2, int(n**0.5) + 1):
            if(n%i==0):
                return False
        return True
        
def arePerm(i,j,k):
	i=sorted(str(i))
	j=sorted(str(j))
	k=sorted(str(k))
	if(i==j and j==k):
		return True
	return False
	
minN=1000
maxN=10000
found=0
targetFound=2
primes=listPrimes(maxN)
while(found<targetFound):
	for p in primes:
		#restrict delta
		for d in range(1,int((maxN-p)/2)):
			i=p
			j=i+d
			k=i+2*d
			#i is already prime
			if(isPrime(j) and isPrime(k)):
				if(arePerm(i,j,k,)):
					found+=1
					if(found==targetFound):
						print(i,j,k)
					break
		if(found==targetFound):
			break	