#<p>We shall say that an $n$-digit number is pandigital if it makes use of all the digits $1$ to $n$ exactly once; for example, the $5$-digit number, $15234$, is $1$ through $5$ pandigital.</p>
#<p>The product $7254$ is unusual, as the identity, $39 \times 186 = 7254$, containing multiplicand, multiplier, and product is $1$ through $9$ pandigital.</p>
#<p>Find the sum of all products whose multiplicand/multiplier/product identity can be written as a $1$ through $9$ pandigital.</p>
#<div class="note">HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.</div>

# CASE 1. (a - 2-digit) and (b - 3-digit) 
sum=0
found=[]

#a and b can be restricted
for a in range(1,100):
    for b in range(100,10000):
        p=a*b
        #len(p) can be maximum 5
        if(len(str(p))>5):
        	 break  
        allDigits = sorted(str(p)+str(a)+str(b))
    
        if(allDigits == list('123456789')):
            if(p not in found):
                found+=[p]
                sum+=p            
print(sum)