#<p>Pentagonal numbers are generated by the formula, $P_n=n(3n-1)/2$. The first ten pentagonal numbers are:
#$$1, 5, 12, 22, 35, 51, 70, 92, 117, 145, \dots$$</p>
#<p>It can be seen that $P_4 + P_7 = 22 + 70 = 92 = P_8$. However, their difference, $70 - 22 = 48$, is not pentagonal.</p>
#<p>Find the pair of pentagonal numbers, $P_j$ and $P_k$, for which their sum and difference are pentagonal and $D = |P_k - P_j|$ is minimised; what is the value of $D$?</p>
import math 

def pent(n):
	return int(n*(3*n-1)/2)
	
def isPent(n):
    #use inverse formula
    res=(math.sqrt(24*n+1)+1)/6
    return res.is_integer() and res>0

flag=True
i=1
d=0
while flag:
    for j in range(1, i):
        a=pent(i)
        b=pent(j)
        if(isPent(a+b) and isPent(a-b)):
            d=abs(a-b)
            flag=False
            break
    i+=1

print(d)	