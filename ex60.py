#<p>The primes $3$, $7$, $109$, and $673$, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking $7$ and $109$, both $7109$ and $1097$ are prime. The sum of these four primes, $792$, represents the lowest sum for a set of four primes with this property.</p>
#<p>Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.</p
from itertools import permutations
import math, random

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

def check(a,b):
	return isPrime(int(str(a)+str(b))) and isPrime(int(str(b)+str(a)))
	
#the key to achieve performance in terms of computational time is to consider primes 2-by-2 and check the permutations. Once two primes satisfy the requirements, we can check each one of them with the new primes, etc                                  
def sol():
    #performance depends on magnituted of nMax
    #value found after several attempts
    nMax=10000
    p=listPrimes(nMax)
    #using number 2 doesn't make sense, skip it
    for i in range(1,len(p)-4):
        #restrict indeces
        for j in range(i+1, len(p)-3):
            if(check(p[i],p[j])):
                for k in range(j+1, len(p)-2):
                    if(check(p[i],p[k]) and check(p[j],p[k])):
                        for l in range(k+1, len(p)-1):
                            if(check(p[i],p[l]) and check(p[j],p[l]) and check(p[k],p[l])):
                                for m in range(l+1, len(p)):
                                    if(check(p[i],p[m]) and check(p[j],p[m]) and check(p[k],p[m]) and check(p[l], p[m])):
                                        return p[i]+p[j]+p[k]+p[l]+p[m]

print(sol())					