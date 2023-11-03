#The prime factors of $13195$ are $5, 7, 13$ and 29
#What is the largest prime factor of the number 600851475143?

factors = []
div = 2
n=600851475143
while div <= n:
	if(n%div== 0):
		factors.append(div)
		n = n/div
	else:
		div = div+1
print(factors[len(factors)-1])