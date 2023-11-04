#Starting in the top left corner of a $2 \times 2$ grid, and only being able to move to the right and down, there are exactly $6$ routes to the bottom right corner.
#How many such routes are there through a $20 \times 20$ grid?

#a brute-force method can be avoided.
#the problem can be reduced to a binomial coefficent C(a+b,a)=(a+b)!/(a!b!)) where a and b are the lattice dimensions
from math import factorial

def binCoeff(latticeDims):
	return factorial(latticeDims[0]+latticeDims[1])/(factorial(latticeDims[0])*factorial(latticeDims[1]))

maxDim=20

for i in range(2,maxDim+1):
	print(i,"*",i," lattice: ",binCoeff([i,i]))
