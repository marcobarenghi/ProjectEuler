#<p>An irrational decimal fraction is created by concatenating the positive integers:
#$$0.12345678910{\color{red}\mathbf 1}112131415161718192021\cdots$$</p>
#<p>It can be seen that the $12$<sup>th</sup> digit of the fractional part is $1$.</p>
#<p>If $d_n$ represents the $n$<sup>th</sup> digit of the fractional part, find the value of the following expression.
#$$d_1 \times d_{10} \times d_{100} \times d_{1000} \times d_{10000} \times d_{100000} \times d_{1000000}$$</p>
import time

#method 1 - semi-brute force
n=""
i=1
desiredPos=[0,9,99,999,9999,99999,999999]
product=1

start1=time.time()
while(len(n)<desiredPos[-1]+1):
	n+=str(i)
	i+=1 
for d in desiredPos:
	product*=int(n[d])
stop1=time.time()
print("Method1", product)

#method 2 - avoid creating 100000 digits number
#use position "offsets"
n=""
i=1
desiredPos=[0,9,99,999,9999,99999,999999]
product=1
currPos=0
prevPos=0

start2=time.time()
while(currPos<desiredPos[-1]+1):
	n=str(i)
	currPos+=len(n)
	for d in desiredPos:
		if(prevPos<=d and currPos>d):
			product*=int(n[prevPos-d])
	prevPos=currPos
	i+=1
stop2=time.time()
print("Method2", product)

print("Time performance ration", int((stop1-start1)/(stop2-start2)))