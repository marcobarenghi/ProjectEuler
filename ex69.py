#<p>Euler's totient function, $\phi(n)$ [sometimes called the phi function], is defined as the number of positive integers not exceeding $n$ which are relatively prime to $n$. For example, as $1$, $2$, $4$, $5$, $7$, and $8$, are all less than or equal to nine and relatively prime to nine, $\phi(9)=6$.</p>
#<div class="center">
#<table class="grid center"><tr><td><b>$n$</b></td>
#<td><b>Relatively Prime</b></td>
#<td><b>$\phi(n)$</b></td>
#<td><b>$n/\phi(n)$</b></td>
#</tr><tr><td>2</td>
#<td>1</td>
#<td>1</td>
#<td>2</td>
#</tr><tr><td>3</td>
#<td>1,2</td>
#<td>2</td>
#<td>1.5</td>
#</tr><tr><td>4</td>
#<td>1,3</td>
#<td>2</td>
#<td>2</td>
#</tr><tr><td>5</td>
#<td>1,2,3,4</td>
#<td>4</td>
#<td>1.25</td>
#</tr><tr><td>6</td>
#<td>1,5</td>
#<td>2</td>
#<td>3</td>
#</tr><tr><td>7</td>
#<td>1,2,3,4,5,6</td>
#<td>6</td>
#<td>1.1666...</td>
#</tr><tr><td>8</td>
#<td>1,3,5,7</td>
#<td>4</td>
#<td>2</td>
#</tr><tr><td>9</td>
#<td>1,2,4,5,7,8</td>
#<td>6</td>
#<td>1.5</td>
#</tr><tr><td>10</td>
#<td>1,3,7,9</td>
#<td>4</td>
#<td>2.5</td>
#</tr></table></div>
#<p>It can be seen that $n = 6$ produces a maximum $n/\phi(n)$ for $n\leq 10$.</p>
#<p>Find the value of $n\leq 1\,000\,000$ for which $n/\phi(n)$ is a maximum.</p>
from functools import reduce

def listPrimes(n):
    primes=[True]*(n+1)
    primes[0]=False
    primes[1]=False

    for i in range(2, int(n**0.5)+1):
        if(primes[i]):
            for j in range(i*i, n+1, i):
                primes[j]=False

    return [num for num, isPrime in enumerate(primes) if isPrime]

#by studying the result of the brute-force attempts, one can observe that n with highest n/phi(n) was always given by the product of all primes (with product<nMax)
#with a quick calculation, one can see that primes up to 17 are enough for our calc.
primes=listPrimes(18) 
nMax=1000000
n=1
for p in primes:
  #continue until n reaches/exceeds nMax
  #n*nextPrime cant be >=  nMax
  if(n>=(nMax+p-1)/p):
  	break
  n*=p
print(n)
#test, to prove my assumption
print(reduce(lambda x, y: x * y, primes)==n)
  
#########################################
#this was my brute force method, way too slow already with maxN=1000
#def listNotPrimes(n):
#    primes=[True]*(n+1)
#    primes[0]=False
#    primes[1]=False

#    for i in range(2, int(n**0.5)+1):
#        if(primes[i]):
#            for j in range(i*i, n+1, i):
#                primes[j]=False

#    return [num for num, isPrime in enumerate(primes) if not isPrime]
          
#excluding 1 and n itself
#def listDivisors(n):
#    d=[]
#    i=2
#    while(i<=int((n+1)/2)):
#    	if(n%i==0):
#    		d.append(i)
#    	i+=1
#    return d

#this was my brute force method, way too slow already with maxN=1000
# #calc n/phi(n)   
#def calcRatio(n):
#	#1 is always relatively prime
#	listDivisorsN=listDivisors(n)
#	count=1	
#	if(n%2==0):
#		#if n is odd, skip even numbers
#		for i in range(3,n,2):
#			listDivisorsTmp=listDivisors(i)			
#			if(set(listDivisorsN).isdisjoint(listDivisorsTmp) and i not in listDivisorsN):
#				count+=1
#	else:
#			#2 is always relatively prime to odd numbers
#		count+=1
#		for i in range(3,n):
#			listDivisorsTmp=listDivisors(i)			
#			if(set(listDivisorsN).isdisjoint(listDivisorsTmp) and i not in listDivisorsN):
#				count+=1
#			
#	return n/count
#					                      
#nMax=500
#prime number will produce low phi(n) values, approaching 1 as n increases
#notPrimes=listNotPrimes(nMax)
#n=0
#maxRatio=0
#for i in range(3,len(notPrimes)):
#	r=calcRatio(notPrimes[i])
#	if(maxRatio<r):
#		n=notPrimes[i]
#		maxRatio=r
#		
#print(n, maxRatio)