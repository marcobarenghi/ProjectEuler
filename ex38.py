#<p>Take the number $192$ and multiply it by each of $1$, $2$, and $3$:</p>
#\begin{align}
#192 \times 1 &amp;= 192\\
#192 \times 2 &amp;= 384\\
#192 \times 3 &amp;= 576
#\end{align}
#<p>By concatenating each product we get the $1$ to $9$ pandigital, $192384576$. We will call $192384576$ the concatenated product of $192$ and $(1,2,3)$.</p>
#<p>The same can be achieved by starting with $9$ and multiplying by $1$, $2$, $3$, $4$, and $5$, giving the pandigital, $918273645$, which is the concatenated product of $9$ and $(1,2,3,4,5)$.</p>
#<p>What is the largest $1$ to $9$ pandigital $9$-digit number that can be formed as the concatenated product of an integer with $(1,2, \dots, n)$ where $n \gt 1$?</p>

def isPandigital(n, nDigits):
	digits = set(n)
	return len(digits)==len(str(n)) and '0' not in digits and len(digits)==nDigits

maxPandigital=0
maxDigits=9
for i in range(1,10000):
	#i*1=i
	currVal=str(i)
	currMultiplier=1
	ok=isPandigital(currVal, len(currVal))
	while(len(str(currVal))<10 and ok):
		currMultiplier+=1
		if(len(currVal+str(i*currMultiplier))<10):
			currVal+=str(i*currMultiplier)
			ok=isPandigital(currVal, len(currVal))			
		else:
			break		
	if(int(currVal)>maxPandigital and ok):
		maxPandigital=int(currVal)
		
print(maxPandigital)