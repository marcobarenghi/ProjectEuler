#<p>Consider the fraction, $\dfrac n d$, where $n$ and $d$ are positive integers. If $n \lt d$ and $\operatorname{HCF}(n,d)=1$, it is called a reduced proper fraction.</p>
#<p>If we list the set of reduced proper fractions for $d \le 8$ in ascending order of size, we get:
#$$\frac 1 8, \frac 1 7, \frac 1 6, \frac 1 5, \frac 1 4, \frac 2 7, \frac 1 3, \frac 3 8, \mathbf{\frac 2 5}, \frac 3 7, \frac 1 2, \frac 4 7, \frac 3 5, \frac 5 8, \frac 2 3, \frac 5 7, \frac 3 4, \frac 4 5, \frac 5 6, \frac 6 7, \frac 7 8$$</p>
#<p>It can be seen that $\dfrac 2 5$ is the fraction immediately to the left of $\dfrac 3 7$.</p>
#<p>By listing the set of reduced proper fractions for $d \le 1\,000\,000$ in ascending order of size, find the numerator of the fraction immediately to the left of $\dfrac 3 7$.</p>
import math

higherLimitFraction=3/7
currentClosest=2/5
bestNum=2
bestDen=5
nMax=1000000
#there is no need to write to complete for loop to check every possible fraction. The key is to calculate the num close to the desired fraction.
for den in range(bestDen+1,nMax):
	num=int(den*higherLimitFraction)
	f=num/den
	while(True):
		if(f<higherLimitFraction):
			#proper reduced fraction
			if(math.gcd(num,den)==1):
				if(f>currentClosest):
					currentClosest=f
					bestNum=num
					bestDen=den
					break
				else:
					break
			else:
				num-=1
				f=num/den
		else:
			num-=1
			f=num/den
			
print("Best fraction ", bestNum,"/",bestDen,"=", bestNum/bestDen, " - diff =", higherLimitFraction-bestNum/bestDen)