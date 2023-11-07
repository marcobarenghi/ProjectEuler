#$n!$ means $n \times (n - 1) \times \cdots \times 3 \times 2 \times 1$.
#For example, $10! = 10 \times 9 \times \cdots \times 3 \times 2 \times 1 = 3628800$,<br>and the sum of the digits in the number $10!$ is $3 + 6 + 2 + 8 + 8 + 0 + 0 = 27$
#Find the sum of the digits in the number $100!$.
def factorial(n):
	product=1
	while(n>1):
		product*=n
		n-=1
	return product
		
n=100
p=str(factorial(n))
sum=0
for i in range(len(p)):
	sum+=int(p[i])
	
print(sum)