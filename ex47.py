#<p>The first two consecutive numbers to have two distinct prime factors are:</p>
#\begin{align}
#14 &amp;= 2 \times 7\\
#15 &amp;= 3 \times 5.
#\end{align}
#<p>The first three consecutive numbers to have three distinct prime factors are:</p>
#\begin{align}
#644 &amp;= 2^2 \times 7 \times 23\\
#645 &amp;= 3 \times 5 \times 43\\
#646 &amp;= 2 \times 17 \times 19.
#\end{align}
#<p>Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?</p>

def findDivs(n):
	d= []    
	while(n>1):
		for i in range(2, n+1):
			if(n%i== 0):
				d.append(i)
				n=int(n/i)
				break
	return d
	
def isPrime(n):
    if(n==2):
        return True
    else:
        for i in range(2, int(n**0.5) + 1):
            if(n%i==0):
                return False
        return True

def checkDivs(nDivs, d):
	if(len(d)<nDivs):
		return False
	d=list(set(d))	
	if(len(d)!=nDivs):
		return False		
	for i in range(len(d)):
		if(not isPrime(d[i])):
			return False
	return True
	
nConsecutives=4
nDivs=4
i=130000
count=0
n=0

while(True):
	d=findDivs(i)
	if(checkDivs(nDivs,d)):
		count+=1
		for j in range(1,nConsecutives):
			d2=findDivs(i+j)
			if(checkDivs(nDivs,d2)):
				count+=1
			else:
				i+=count
				count=0
				break
		if(count==nConsecutives):
			print(i)
			break
	else:
		i+=1
	
	