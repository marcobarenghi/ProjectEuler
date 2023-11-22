#<p>Consider quadratic Diophantine equations of the form:
#$$x^2 - Dy^2 = 1$$</p>
#<p>For example, when $D=13$, the minimal solution in $x$ is $649^2 - 13 \times 180^2 = 1$.</p>
#<p>It can be assumed that there are no solutions in positive integers when $D$ is square.</p>
#<p>By finding minimal solutions in $x$ for $D = \{2, 3, 5, 6, 7\}$, we obtain the following:</p>
#\begin{align}
#3^2 - 2 \times 2^2 &amp;= 1\\
#2^2 - 3 \times 1^2 &amp;= 1\\
#{\color{red}{\mathbf 9}}^2 - 5 \times 4^2 &amp;= 1\\
#5^2 - 6 \times 2^2 &amp;= 1\\
#8^2 - 7 \times 3^2 &amp;= 1
#\end{align}
#<p>Hence, by considering minimal solutions in $x$ for $D \le 7$, the largest $x$ is obtained when $D=5$.</p>
#<p>Find the value of $D \le 1000$ in minimal solutions of $x$ for which the largest value of $x$ is obtained.</p>

from math import sqrt
#this equation is know as Pell's equation, see https://en.m.wikipedia.org/wiki/Pell%27s_equation.
#solution can be found by via the regular continued fraction of sqrt(D).

def cf(n):
	mn=0.0
	dn=1.0
	a0=int(sqrt(n))
	an=int(sqrt(n))
	terms=[a0]
	if(a0!=sqrt(n)):
		while(an!=2*a0):
			mn=dn*an-mn
			dn=(n-mn**2)/dn
			an=int((a0+mn)/dn)
			terms.append(an)
	#last conv term is not needed
	return terms[:-1]

#use cf terms to build fraction
def reverseCF(cf):
	num=1
	den=cf.pop()
	while(cf):
		den, num=den*cf.pop()+num, den
	return den, num

D=0
maxX=0
nMax=1000
for d in range(2, nMax+1):
	if(not sqrt(d).is_integer()):
		cf_=cf(d)
		if(len(cf_)%2!=0):
			x, y=reverseCF(cf_)
			#Baskara's Lemma if period of cf_ is odd
			x, y=2*x**2+1, 2*x*y		
		else:
			x, y=reverseCF(cf_)
		assert(x**2-d*y**2==1)
		if(x>maxX):
			D=d
			maxX=x
		
print(D)