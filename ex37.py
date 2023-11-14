#<p>The number $3797$ has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: $3797$, $797$, $97$, and $7$. Similarly we can work from right to left: $3797$, $379$, $37$, and $3$.</p>
#<p>Find the sum of the only eleven primes that are both truncatable from left to right and right to left.</p>
#<p class="smaller">NOTE: $2$, $3$, $5$, and $7$ are not considered to be truncatable primes.</p>

#NOTE: I solve this problem using nMax as costant. An even more generic approach would be to update the prime list until the 11 magic numbers are found. 

def listPrimes(limit):
    array=[True for i in range(limit+1)]
    primes=[]
    p=2
    while(p**2<limit):
    	if(array[p]==True):
    		for i in range(p**2, limit+1,p):
    			array[i]=False
    	p+=1
    for p in range(2, limit+1):
    	if(array[p]):
    		primes.append(p)
    return primes
    
#we should remove all elements that contain at least an even digit -> not all its truncations will be primes
#same goes for digit 5.
#BUT this holds if n>100.
#this is essential, otherwise calculations would take too long
def cleanPrimeList(list):
	i=0
	while(i<len(list)):
		if(list[i]>100):
			tmp=str(list[i])
			for j in range(len(tmp)):
				if(int(tmp[j])%2==0 or int(tmp[j])%5==0):
					list.remove(list[i])
					i-=1
					break
					
		i+=1
	return list

nMax=1000000
primes=listPrimes(nMax)
primes=cleanPrimeList(primes)
sum=0
n=0
i=4
nTarget=11

while(n<nTarget):
	if(primes[i]>10):
		tmp=str(primes[i])
		tmp2=str(primes[i])
		ok=True
		while(len(tmp)>1):
			tmp=tmp[1:]
			tmp2=tmp2[:-1]
			if(len(tmp)>0):
				if(int(tmp) not in primes or int(tmp2) not in primes):
					ok=False
					break		
		if(ok):
			sum+=primes[i]
			n+=1
	i+=1
		
print(sum)