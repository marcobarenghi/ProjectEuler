#A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99.
#Find the largest palindrome made from the product of two $3$-digit numbers.

maxPalim = 0
for i in range(100,1000):
	for j in range(i,1000):
		val = str(i*j)
		if(len(val)%2==0):
			if(val[:len(val)/2]==val[len(val)/2:]):
				if(i*j > maxPalim):
					maxPalim = i*j
		else:
			a=1
			
print(maxPalim)