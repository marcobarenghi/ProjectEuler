#<p>It is possible to write ten as the sum of primes in exactly five different ways:</p>
#\begin{align}
#&amp;7 + 3\\
#&amp;5 + 5\\
#&amp;5 + 3 + 2\\
#&amp;3 + 3 + 2 + 2\\
#&amp;2 + 2 + 2 + 2 + 2
#\end{align}
#<p>What is the first value which can be written as the sum of primes in over five thousand different ways?</p>

def listPrimes(n):
    primes=[True]*(n+1)
    primes[0]=False
    primes[1]=False

    for i in range(2, int(n**0.5)+1):
        if(primes[i]):
            for j in range(i*i, n+1, i):
                primes[j]=False

    return [num for num, isPrime in enumerate(primes) if isPrime]
        
#this is similar to ex76, as the combinations of the sums of n can be calculate knowing the result of the lower numbers  
#primes up to 100 are enough
primes=listPrimes(100)
print(primes)
targetLength=5000
n=2
while(True):
	combs=[1]+[0]*n
	for p in primes:
		for i in range(p, n+1):
			combs[i]+=combs[i-p]
	if(combs[n]>targetLength):
		print(n)
		break
	n+=1
