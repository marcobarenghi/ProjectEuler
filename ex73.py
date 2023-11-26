#<p>Consider the fraction, $\dfrac n d$, where $n$ and $d$ are positive integers. If $n \lt d$ and $\operatorname{HCF}(n, d)=1$, it is called a reduced proper fraction.</p>
#<p>If we list the set of reduced proper fractions for $d \le 8$ in ascending order of size, we get:
#$$\frac 1 8, \frac 1 7, \frac 1 6, \frac 1 5, \frac 1 4, \frac 2 7, \frac 1 3, \mathbf{\frac 3 8, \frac 2 5, \frac 3 7}, \frac 1 2, \frac 4 7, \frac 3 5, \frac 5 8, \frac 2 3, \frac 5 7, \frac 3 4, \frac 4 5, \frac 5 6, \frac 6 7, \frac 7 8$$</p>
#<p>It can be seen that there are $3$ fractions between $\dfrac 1 3$ and $\dfrac 1 2$.</p>
#<p>How many fractions lie between $\dfrac 1 3$ and $\dfrac 1 2$ in the sorted set of reduced proper fractions for $d \le 12\,000$?</p>
import math

upperLimit=1/2
lowerLimit=1/3
nMax=12000
count=0

for den in range(4,nMax+1):
	#calculate starting num for each den, decrease num as long as the fraction value is inside the limit
	if(den%2==0):
		num=int(den*upperLimit-1)
	else:
		num=int(den*upperLimit)
	f=num/den
	while(f>lowerLimit and f<upperLimit):
		if(math.gcd(num,den)==1):
			count+=1
		num-=1
		f=num/den
		
print(count)