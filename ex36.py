#<p>The decimal number, $585 = 1001001001_2$ (binary), is palindromic in both bases.</p>
#<p>Find the sum of all numbers, less than one million, which are palindromic in base $10$ and base $2$.</p>
#<p class="smaller">(Please note that the palindromic number, in either base, may not include leading zeros.)</p>
#solution to add the values for each iteration
count=0

nMax=1000000
#looping through odd numbers
for i in range(1,nMax,2):
	#checking base 10 number
	if(str(i)==str(i)[::-1]):
		#checking base 2 number
		if(bin(i)[2:]==bin(i)[2:][::-1]):
			count+=i

print(count)