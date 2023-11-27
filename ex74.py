#<p>The number $145$ is well known for the property that the sum of the factorial of its digits is equal to $145$:
#$$1! + 4! + 5! = 1 + 24 + 120 = 145.$$</p>
#<p>Perhaps less well known is $169$, in that it produces the longest chain of numbers that link back to $169$; it turns out that there are only three such loops that exist:</p>
#\begin{align}
#&amp;169 \to 363601 \to 1454 \to 169\\
#&amp;871 \to 45361 \to 871\\
#&amp;872 \to 45362 \to 872
#\end{align}
#<p>It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,</p>
#\begin{align}
#&amp;69 \to 363600 \to 1454 \to 169 \to 363601 (\to 1454)\\
#&amp;78 \to 45360 \to 871 \to 45361 (\to 871)\\
#&amp;540 \to 145 (\to 145)
#\end{align}
#<p>Starting with $69$ produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.</p>
#<p>How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?</p>
#meomization allows to gain ~100x speed if compared to brute force method
def f(n):
	if(n==0 or n==1):
		return 1
	else:
		p=1
		while(n>1):
			p*=n
			n-=1
		return p
			
def digitsSumFactorial(n):
	sum=0
	for i in range(len(str(n))):
		sum+=f(int(str(n)[i]))
	return sum
	
def chainLength(n, memo):
	c=[n]
	while(True):
		n=digitsSumFactorial(n)
		#for each case, memo must be updated accordingly
		#case1: n is repeated in the chain
		if(n in c):
			for num in c:
				memo[num]=len(c)-c.index(num)
			return len(c)
		#case2: n is found in the cache
		elif(n in memo):
			i=0
			for num in c:
				memo[num]=memo[n]+(len(c)-i)
				i+=1
			return len(c)+memo[n]
			#case3: n is "new"
		else:
			c.append(n)
		
def countChainLength(nMax, targetL):
	#dict to cache already explored values
	memo={}
	count=0
	for n in range(1,nMax):
		if(chainLength(n,memo)==targetL):
			count+=1
	return count

nMax=1000000
targetL=60	
res=countChainLength(nMax, targetL)
print(res)