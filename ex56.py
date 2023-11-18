#<p>A googol ($10^{100}$) is a massive number: one followed by one-hundred zeros; $100^{100}$ is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only $1$.</p>
#<p>Considering natural numbers of the form, $a^b$, where $a, b \lt 100$, what is the maximum digital sum?</p>

maxN=99
sum=0
for i in range(1,maxN+1):
	for j in range(1,maxN+1):
		n=str(i**j)
		sumTmp=0
		for k in range(len(n)):
			sumTmp+=int(n[k])
		if(sumTmp>sum):
			sum=sumTmp
			
print(sum)
		
		
		
	