#<p>The fraction $49/98$ is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that $49/98 = 4/8$, which is correct, is obtained by cancelling the $9$s.</p>
#<p>We shall consider fractions like, $30/50 = 3/5$, to be trivial examples.</p>
#<p>There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.</p>
#<p>If the product of these four fractions is given in its lowest common terms, find the value of the denominator.</p>
import math

num=1
denom=1
for d in range(10, 100):
	for n in range(10, d):
		#decompose n and d without using strings
		#n =10*n1+n0
		#d =10*d1+d0 
		n0 =n%10
		n1=n//10
		d0=d % 10
		d1=d//10
		#do not consider trivial cases
		if (n1==d0 and n0*d==n*d1) or (n0==d1 and n1*d==n*d0):
			num*=n
			denom*=d
#use greatest common denom function to find solution
print((denom//math.gcd(num, denom)))