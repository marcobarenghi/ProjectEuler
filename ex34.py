#<p>$145$ is a curious number, as $1! + 4! + 5! = 1 + 24 + 120 = 145$.</p>
#<p>Find the sum of all numbers which are equal to the sum of the factorial of their digits.</p>
#<p class="smaller">Note: As $1! = 1$ and $2! = 2$ are not sums they are not included.</p>

def factorial(n):
	p=1
	while(n>1):
		p*=n
		n-=1
	return p

sum=0
for i in range(10,100000):
	tmp=str(i)
	sumTmp=0
	for j in range(len(tmp)):
		sumTmp+=factorial(int(tmp[j]))
	if(sumTmp==i):
		sum+=i

print(sum)
		