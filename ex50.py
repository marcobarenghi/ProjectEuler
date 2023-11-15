#<p>The prime $41$, can be written as the sum of six consecutive primes:</p>
#$$41 = 2 + 3 + 5 + 7 + 11 + 13.$$
#<p>This is the longest sum of consecutive primes that adds to a prime below one-hundred.</p>
#<p>The longest sum of consecutive primes below one-thousand that adds to a prime, contains $21$ terms, and is equal to $953$.</p>
#<p>Which prime, below one-million, can be written as the sum of the most consecutive primes?</p

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
        
maxN=1000000
primes=listPrimes(maxN)
#length of consecutive primes sum
length=0
n=0
index=len(primes)

#loop through primes
for i in range(len(primes)):
    #define range to sum
    for j in range(i+length, index):
        tmp=sum(primes[i:j])
        if(tmp<maxN):
            if(isPrime(tmp)):
                length=j-i
                n=tmp
        else:
            index=j+1
            break

print(n, length)	
	
	
	