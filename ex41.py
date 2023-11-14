#<p>We shall say that an $n$-digit number is pandigital if it makes use of all the digits $1$ to $n$ exactly once. For example, $2143$ is a $4$-digit pandigital and is also prime.</p>
#<p>What is the largest $n$-digit pandigital prime that exists?</p>
from itertools import permutations

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if(n%i==0):
            return False
    return True
    
digits="123456789"

flag=True
#let us start with 9 digits
nDigits=9
while(flag):
    p=permutations(digits[:nDigits])
    p=list(p)[::-1]
    for i in p:
        #discard even numbers
        if(int(i[nDigits-1])%2!=0):
            n=int(''.join(i))
            if(isPrime(n)):
            	print(n)
            	flag=False
            	break
    #if no perm if found, list of digits is shrinks down
    nDigits-=1