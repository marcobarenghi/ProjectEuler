# see https://en.m.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
#given m>n >0, coprime and not both odd, one can form a Pythagorean triple as follows: #a=m**2-n**2, b=2mn, c=m**2+n**2.
#indentation issues fixed with chatgpt
from collections import Counter
from math import gcd
from itertools import count

#use of yield statement is necessary for the performance of this problem
#yield allows to create a generator function and producing values on-the-fly without having to store them at once. Values are computed only when requested (lazy evaluation)
def calcEdges():
	m = 1
	while True:
		for n in range(1, m):
			if (m + n) % 2 and gcd(m, n) == 1:
				a = m**2 - n**2
				b = 2 * m * n
				c = m**2 + n**2
				d = 2 * m * (m + 1)
				yield a, b, c, d
		m += 1

def sol(nMax):
	triangles = Counter()
	for a, b, c, d in calcEdges():
		if d > nMax:
			break
		p = a + b + c
		for i in range(p, pMax + 1, p):
			triangles[i] += 1
	return sum(n == 1 for n in triangles.values())

#def calcEdges():
#    m = 1
#    results = []
#    while True:
#        for n in range(1, m):
#            if (m + n) % 2 and gcd(m, n) == 1:
#                a = m**2 - n**2
#                b = 2 * m * n
#                c = m**2 + n**2
#                d = 2 * m * (m + 1)
#                results.append((a, b, c, d))
#        m += 1
#    return results

#def sol(nMax):
#    triangles = Counter()
#    edges = calcEdges()
#    for a, b, c, d in edges:
#        if d > nMax:
#            break
#        p = a + b + c
#        for i in range(p, nMax + 1, p):
#            triangles[i] += 1
#    return sum(n == 1 for n in triangles.values())	

pMax=1500000
print(sol(pMax))