#<p>Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#\begin{align}
#1634 &amp;= 1^4 + 6^4 + 3^4 + 4^4\\
#8208 &amp;= 8^4 + 2^4 + 0^4 + 8^4\\
#9474 &amp;= 9^4 + 4^4 + 7^4 + 4^4
#\end{align}
#</p><p class="smaller">As $1 = 1^4$ is not a sum it is not included.</p>
#<p>The sum of these numbers is $1634 + 8208 + 9474 = 19316$.</p>
#<p>Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.</p>

def sum(nMin, nMax, exp):
	totSum=0
	for n in range(nMin, nMax+1):
		num=str(n)
		sum=0
		for i in range(len(num)):
			sum+=int(num[i])**exp
		if(sum==n):
			totSum+=n
	print(totSum-1)

#last number already known
sum(1,9474, 4)
#the only consideration that must be taken into account is the upper limit.
#k*9^5. where k=5
sum(1,5*(9**5), 5)
		
