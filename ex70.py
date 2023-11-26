#<p>Euler's totient function, $\phi(n)$ [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to $n$ which are relatively prime to $n$. For example, as $1, 2, 4, 5, 7$, and $8$, are all less than nine and relatively prime to nine, $\phi(9)=6$.<br>The number $1$ is considered to be relatively prime to every positive number, so $\phi(1)=1$. </p>
#<p>Interestingly, $\phi(87109)=79180$, and it can be seen that $87109$ is a permutation of $79180$.</p>
#<p>Find the value of $n$, $1 \lt n \lt 10^7$, for which $\phi(n)$ is a permutation of $n$ and the ratio $n/\phi(n)$ produces a minimum.</p>
def listPrimes(n):
    primes=[True]*(n+1)
    primes[0]=False
    primes[1]=False

    for i in range(2, int(n**0.5)+1):
        if(primes[i]):
            for j in range(i*i, n+1, i):
                primes[j]=False

    return [num for num, isPrime in enumerate(primes) if isPrime]
	
def sol(nMax):
    #hack is to consider n as product of primes (idea comes from solution of ex69
    #it is enough to restrict primes to 50%>sqrt(nMax)
    primes=listPrimes(int(1.5*nMax**0.5))
    minRatio=100000000
    n=1
    for p1 in primes:
        for p2 in primes:
            if(p1*p2<nMax):
                #phi(n)=phi(p1*p2)=(p1-1)*(p2-1)
                #and we must check that n and phi(n) are permutations of each other
                if(sorted(list(str(p1*p2)))==sorted(list(str((p1-1)*(p2-1))))):
                    if((p1*p2)/((p1-1)*(p2-1))<minRatio):
                        minRatio=(p1*p2)/((p1-1)*(p2-1))
                        n=p1*p2
    return n
    
nMax=10000000                
print(sol(nMax))