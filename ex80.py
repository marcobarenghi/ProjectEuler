#<p>It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.</p>
#<p>The square root of two is $1.41421356237309504880\cdots$, and the digital sum of the first one hundred decimal digits is $475$.</p>
#<p>For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.</p>
from decimal import *
import math

nDigits=100
nMax=100
getcontext().prec=nDigits+2

sum=0
for n in range(2,nMax):
	value=Decimal(n).sqrt()
	if(not float(value).is_integer()):
		for i in range(2,nDigits+1):
			sum+=int(str(value)[i])
		sum+=int(str(value)[0])
			
print(sum)