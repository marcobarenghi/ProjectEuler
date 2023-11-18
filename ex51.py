#<p>By replacing the 1<sup>st</sup> digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.</p>
#<p>By replacing the 3<sup>rd</sup> and 4<sup>th</sup> digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.</p>
#<p>Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.</p>

from collections import Counter

def listPrimes(n):
    primes=[True]*(n+1)
    primes[0]=False
    primes[1]=False

    for i in range(2, int(n**0.5)+1):
        if(primes[i]):
            for j in range(i*i, n+1, i):
                primes[j]=False

    return [num for num, isPrime in enumerate(primes) if isPrime]

#finds parts to substitute and creates list with all possibilities  
def substituteAndCreateList(s):
    s=str(s)
    list=[]
    a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for duplicate in (Counter(s)-Counter(set(s))):   
        temp=[int(s.replace(duplicate, x)) for x in a]
        list.append(temp)
    return list
  
#removes non-prime numbers 
def cleanList(l):
    for i in l:
        checked.append(i)
        if i not in primes:
            l.remove(i)
    return l

nMax=1000000
primes=listPrimes(nMax)
# primes with 3 replacable spots
replaceableSpots=3
primes=[x for x in primes if len(str(x)) - len(set(str(x))) >= replaceableSpots]

famSize=8
checked=[]
flag=True
i=0
while flag:
    if(primes[i] not in checked):
        list=substituteAndCreateList(primes[i])
        for j in list:
            if(len(cleanList(j))==famSize):
                print(j[0])
                print("Family: ", j)
                flag=False
                break
    i+=1