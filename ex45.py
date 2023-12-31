#<p>Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:</p>
#<table><tr><td>Triangle</td>
#<td> </td>
#<td>$T_n=n(n+1)/2$</td>
#<td> </td>
#<td>$1, 3, 6, 10, 15, \dots$</td>
#</tr><tr><td>Pentagonal</td>
#<td> </td>
#<td>$P_n=n(3n - 1)/2$</td>
#<td> </td>
#<td>$1, 5, 12, 22, 35, \dots$</td>
#</tr><tr><td>Hexagonal</td>
#<td> </td>
#<td>$H_n=n(2n - 1)$</td>
#<td> </td>
#<td>$1, 6, 15, 28, 45, \dots$</td>
#</tr></table><p>It can be verified that $T_{285} = P_{165} = H_{143} = 40755$.</p>
#<p>Find the next triangle number that is also pentagonal and hexagonal.</p>
import math 

def triangle(n):
	return int(n*(n+1)/2)
	
def reverseTriangle(n):
    res=(math.sqrt(1+8*n)-1)/2
    if(res.is_integer() and res>0):
    	return int(res)
    else:
    	return -1
	
def isPentagonal(n):
	res=(math.sqrt(24*n+1)+1)/6
	return res.is_integer() and res>0
    
def isHexagonal(n):
	res=(math.sqrt(8*n+1)+1)/4
	return res.is_integer() and res>0
	
start=reverseTriangle(40755)

while(True):
	start+=1
	currentRes=triangle(start)
	if(isPentagonal(currentRes) and isHexagonal(currentRes)):
		print(currentRes)
		break
