#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#012   021   102   120   201   210
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

#compare operations timing
import time

#python allows us to use a hacky way of solving this
from itertools import permutations
#generate perm and save the as a list. perms are already ordered.
start1=time.time()
perm=list(permutations('0123456789'))
sol=''.join(perm[999999])
end1=time.time()
print(sol)

#BUT that's not fun. let's find a way that would work with all programming languages
#not all permutations need to be generated, one can use math knowledge solve this 
def factorial(n):
	product=1
	while(n>1):
		product*=n
		n-=1
	return product

start2=time.time()
result = []
digits=[0,1,2,3,4,5,6,7,8,9]
remaining_digits = digits[:]
target = 999999

for i in range(digits[len(digits)-1],-1,-1):
	f=factorial(i)
	#pick index
	index=target//f
	result.append(remaining_digits.pop(index))
	#update target -> it will reach 0 on the last iteration
	target%=f

end2=time.time()
print(''.join(map(str, result)))
print("Performance time ratio method2-method1:", int((end1-start1)/(end2-start2)))


