#Let $d(n)$ be defined as the sum of proper divisors of $n$ (numbers less than $n$ which divide evenly into $n$).
#If $d(a) = b$ and $d(b) = a$, where $a \ne b$, then $a$ and $b$ are an amicable pair and each of $a$ and $b$ are called amicable numbers.
#For example, the proper divisors of $220$ are $1, 2, 4, 5, 10, 11, 20, 22, 44, 55$ and $110$; therefore $d(220) = 284$. The proper divisors of $284$ are $1, 2, 4, 71$ and $142$; so $d(284) = 220$.
#Evaluate the sum of all the amicable numbers under $10000$.

import math

def sumDivisors(n):
    #optimized divisors function
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # Avoid adding the same divisor twice for perfect squares
                divisors.append(n // i)
    #remove n itself
    divisors.remove(n)
    #perform sum
    sum=0
    for i in range(len(divisors)):
    	sum+=divisors[i]
    return sum
	
nMax=10000
#bool array of nMax elements, used for opt.
#couples of amicable numbers are unique
isAmicable=[False]*nMax
sum=0
for i in range(2,nMax):
	if(not isAmicable[i]):
		possibleAmicable=sumDivisors(i)
		if(sumDivisors(possibleAmicable)==i and i!=possibleAmicable):
			isAmicable[i] = True
			isAmicable[possibleAmicable] = True
			print(i, possibleAmicable)
			sum+=i+possibleAmicable
print(sum)