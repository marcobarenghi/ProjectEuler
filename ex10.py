#The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17
#Find the sum of all the primes below two million.

#classical method is too slow -> sieve methods
def sumPrimes(n):
    sum = 0
    sieve = [True] * n
    for i in range(2, n):
        if sieve[i]:
            sum += i
            #print(i)
            for i in range(i*i, n, i):
                sieve[i] = False
    return sum

print(sumPrimes(2000000))