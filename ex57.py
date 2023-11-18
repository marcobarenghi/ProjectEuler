#<p>It is possible to show that the square root of two can be expressed as an infinite continued fraction.</p>
#<p class="center">$\sqrt 2 =1+ \frac 1 {2+ \frac 1 {2 +\frac 1 {2+ \dots}}}$</p>
#<p>By expanding this for the first four iterations, we get:</p>
#<p>$1 + \frac 1 2 = \frac  32 = 1.5$<br>
#$1 + \frac 1 {2 + \frac 1 2} = \frac 7 5 = 1.4$<br>
#$1 + \frac 1 {2 + \frac 1 {2+\frac 1 2}} = \frac {17}{12} = 1.41666 \dots$<br>
#$1 + \frac 1 {2 + \frac 1 {2+\frac 1 {2+\frac 1 2}}} = \frac {41}{29} = 1.41379 \dots$<br></p>
#<p>The next three expansions are $\frac {99}{70}$, $\frac {239}{169}$, and $\frac {577}{408}$, but the eighth expansion, $\frac {1393}{985}$, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.</p>
#<p>In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?</p>

#more info on continued fractions can be found here 
#https://en.m.wikipedia.org/wiki/Continued_fraction

#-> if a/b converges, next convergent can be written as (a+2b)/(a+b)

a=1
b=1
nMax=1000
count=0
for i in range(nMax):
	a1=a+2*b
	b1=a+b
	if(len(str(a1))>len(str(b1))):
		count+=1
	a=a1
	b=b1
print(count)