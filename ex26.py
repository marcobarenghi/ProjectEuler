#<p>A unit fraction contains $1$ in the numerator. The decimal representation of the unit fractions with denominators $2$ to $10$ are given:</p>
#\begin{align}
#1/2 &amp;= 0.5\\
#1/3 &amp;=0.(3)\\
#1/4 &amp;=0.25\\
#1/5 &amp;= 0.2\\
#1/6 &amp;= 0.1(6)\\
#1/7 &amp;= 0.(142857)\\
#1/8 &amp;= 0.125\\
#1/9 &amp;= 0.(1)\\
#1/10 &amp;= 0.1
#\end{align}
#<p>Where $0.1(6)$ means $0.166666\cdots$, and has a $1$-digit recurring cycle. It can be seen that $1/7$ has a $6$-digit recurring cycle.</p>
#<p>Find the value of $d \lt 1000$ for which $1/d$ contains the longest recurring cycle in its decimal fraction part.</p>

def cycleLength(denominator):
	remainders = []
	remainder = 1
	position = 0
	decimals = []

	while(remainder not in remainders and remainder!=0):
		remainders.append(remainder)
		remainder=(remainder * 10)%denominator
		position+=1

		# Calculate the current digit
		decimals.append(remainder * 10 // denominator)

	if(remainder==0):
		return 0, decimals # There is no recurring cycle
	else:
		recurringStart=remainders.index(remainder)
		recurringPart=decimals[recurringStart:]
		#correctly display recurringPart. move last digit in from 
		lastElem=decimals[-1]
		recurringPart = [lastElem]+recurringPart[:-1] 
    
		return position-recurringStart, recurringPart

nMax=1000
n=0
maxLen=0
maxCycle=[]
for i in range(2, nMax):
    l, cycle = cycleLength(i)
    if(l>maxLen):
        maxLen = l
        maxCycle = cycle
        n = i
	
print(f"The cycle length for 1/{n} is: {maxLen}")
print(f"Recurring part: {maxCycle}")