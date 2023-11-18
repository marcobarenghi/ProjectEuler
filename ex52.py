#<p>It can be seen that the number, $125874$, and its double, $251748$, contain exactly the same digits, but in a different order.</p>
#<p>Find the smallest positive integer, $x$, such that $2x$, $3x$, $4x$, $5x$, and $6x$, contain the same digits.</p>
#6 digits->start from 10**6
n=100000
maxMultiplier=6

while(True):
	count=0
	for i in range(2, maxMultiplier+1):
		tmp=n*i
		if(sorted(str(tmp))==sorted(str(n))):
			count+=1
		else:
			break
	if(count==maxMultiplier-1):
		print(n)
		break
	else:
		n+=1
		