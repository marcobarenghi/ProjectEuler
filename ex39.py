#<p>We shall say that an $n$-digit number is pandigital if it makes use of all the digits $1$ to $n$ exactly once. For example, $2143$ is a $4$-digit pandigital and is also prime.</p>
#<p>What is the largest $n$-digit pandigital prime that exists?</p>
import math
from collections import Counter

pMax=1000
aMax=pMax//2
bMax=pMax//2

perimeters=[]

#trigometry knowledge
#a+b+c=p
#c=sqrt(a**2+b**2)
#edge<p/2
for a in range(1, aMax):
	for b in range(1, bMax):
		c=math.sqrt(a**2+b**2)
		perimeters.append(a+b+c)

p = Counter(perimeters)
print(p.most_common(1)[0])