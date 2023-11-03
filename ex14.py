#The following iterative sequence is defined for the set of positive integers:
# is even: n-> n/2
# is odd: n-> 3n+1
#Using the rule above and starting with $13$, we generate the following sequence:
#$$13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1
#It can be seen that this sequence (starting at $13$ and finishing at $1$) contains $10$ terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at $1$.
#Which starting number, under one million, produces the longest chain?
#NOTE:Once the chain starts the terms are allowed to go above one million.

#brute force approach: use this function for every number.
def seq0(n):
	nHelper=n
	count=0
	while nHelper>1:
		if nHelper%2 == 0:
			nHelper/=2
			count+=1
		else:
			nHelper=3*nHelper+1
			count+=1
	return count
	
#nMax=1000000
#maxDepth=0
#n=0	
#for i in range(3, nMax):
#	depth=seq0(i)
#	if(depth>maxDepth):
#		n=i
#		maxDepth=depth
#print(n, maxDepth)

#optimized approach
import sys
#set recursion depth just to be safe
sys.setrecursionlimit(10000)

#caching values avoids to repeat already explored patterns
cache = {}
def seq(n):
	if(not n in cache):
		if(n == 1):
			cache[n] = 1
		elif(n % 2 == 0):
			cache[n] = seq(n // 2) + 1
		else:
			cache[n] = seq(3*n + 1) + 1
	return cache[n]
   
nMax=1000000
maxDepth=0
n=0
for i in range(3,nMax):
	depth=seq(i)
	if(depth>maxDepth):
		n=i
		maxDepth=depth
print(n, maxDepth)
	
