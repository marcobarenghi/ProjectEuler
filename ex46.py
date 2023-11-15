#<p>It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.</p>
#\begin{align}
#9 = 7 + 2 \times 1^2\\
#15 = 7 + 2 \times 2^2\\
#21 = 3 + 2 \times 3^2\\
#25 = 7 + 2 \times 3^2\\
#27 = 19 + 2 \times 2^2\\
#33 = 31 + 2 \times 1^2
#\end{align}
#<p>It turns out that the conjecture was false.</p>
#<p>What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?</p>
import math

def isPrime(n):
    if(n==2):
    	return True
    if(n%2==0):
        return False
    else:
        for i in range(3, int(n**0.5+1),2):
            if(n%i==0):
                return False
        return True

n=3
primes=[2]
while True:
    if(isPrime(n)):
        primes.append(n)
    else:
        ok=False
        for i in primes:
            #the value of (n-prime)/2 must be an int - reverse formula
            test=math.sqrt(((n-i)/2))
            if(test.is_integer()):
                ok=True
                break
        if(not ok):
	        print(n)
	        break

    n+=2
		