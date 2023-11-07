#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of $28$ would be $1 + 2 + 4 + 7 + 14 = 28$, which means that $28$ is a perfect number.
#A number $n$ is called deficient if the sum of its proper divisors is less than $n$ and it is called abundant if this sum exceeds $n$.
#As $12$ is the smallest abundant number, $1 + 2 + 3 + 4 + 6 = 16$, the smallest number that can be written as the sum of two abundant numbers is $24$. By mathematical analysis, it can be shown that all integers greater than $28123$ can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

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

def isAbundant(n):
    if (sumDivisors(n)>n):
        return True
    else:
        return False

nMax=28124

abundentNumbers = []
for i in range(1,nMax):
    if(isAbundant(i)):
        abundentNumbers.append(i)

sums = [0]*nMax
#code takes some time because of this iteration
#opt would be welcome (if possible?)
for x in range (0, len(abundentNumbers)):
    for y in range (x, len(abundentNumbers)):
            sumOf2AbundantNums=abundentNumbers[x]+abundentNumbers[y]
            if(sumOf2AbundantNums<nMax):
                if(sums[sumOf2AbundantNums]==0):
                	sums[sumOf2AbundantNums]=sumOf2AbundantNums

sum=0
for x in range (1,len(sums)):
    #Find the sum of all the positive integers which CANNOT be written as the sum of two abundant numbers.
    if(sums[x]==0):
        sum+=x

print(sum)