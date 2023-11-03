#A Pythagorean triplet is a set of three natural numbers, $a <b < c$, for which,
#$$a^2 + b^2 = c^2
#For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.</p>
#There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.<br>Find the product $abc$.</p>
sum=1000
val=[]
for a in range(1,sum-2):
	for b in range(a+1, sum-3):
			c = sum-a-b
			if(a*a+b*b==c*c):
				print(a,b,c)
				print(a*b*c)
				break
