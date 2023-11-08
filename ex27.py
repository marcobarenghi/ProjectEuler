#<p>Euler discovered the remarkable quadratic formula:</p>
#<p class="center">$n^2 + n + 41$</p>
#<p>It turns out that the formula will produce $40$ primes for the consecutive integer values $0 \le n \le 39$. However, when $n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41$ is divisible by $41$, and certainly when $n = 41, 41^2 + 41 + 41$ is clearly divisible by $41$.</p>
#<p>The incredible formula $n^2 - 79n + 1601$ was discovered, which produces $80$ primes for the consecutive values $0 \le n \le 79$. The product of the coefficients, $-79$ and $1601$, is $-126479$.</p>
#<p>Considering quadratics of the form:</p>
#<blockquote>
#$n^2 + an + b$, where $|a| &lt; 1000$ and $|b| \le 1000$<br><br><div>where $|n|$ is the modulus/absolute value of $n$<br>e.g. $|11| = 11$ and $|-4| = 4$</div>
#</blockquote>
#<p>Find the product of the coefficients, $a$ and $b$, for the quadratic expression that produces the maximum number of primes for consecutive values of $n$, starting with $n = 0$.</p>

def quadratic(a,b,n):
	return n**2+a*n+b

#using 6k+/-1 rule
def isPrime(n):
    if(n<2):
        return False
    if(n<=3):
        return True
    if(n%2==0 or n%3==0):
        return False

    i=5
    w=2
    while(i**2<=n):
        if(n%i==0 or n%(i+2)==0):
            return False
        i+=w
        w =6-w
    return True
    
def listPrimes(n):
	sieve = [True] * (n + 1)
	sieve[0] = sieve[1] = False
	primes = []

	for p in range(2, int(n**0.5) + 1):
		if sieve[p]:
			for i in range(p*p, n+1, p):
				sieve[i] = False

	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)

	return primes
    
maxN1=1000
count=0
a=0
b=0
limit=1000
primes=listPrimes(limit)

for i in range(-maxN1, maxN1):
    #f(0) always returns a prime
    for j in range(len(primes)):
        n=1
        while isPrime(quadratic(i, primes[j], n)):
            n+=1
        if(n>count):
            count=n
            a=i
            b=primes[j]
			
print("a=",a,"| b=",b, " | n=", count)
print("product=", a*b)