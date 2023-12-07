#<p>Let $p(n)$ represent the number of different ways in which $n$ coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so $p(5)=7$.</p>
#<div class="margin_left">
#OOOOO<br>
#OOOO   O<br>
#OOO   OO<br>
#OOO   O   O<br>
#OO   OO   O<br>
#OO   O   O   O<br>
#O   O   O   O   O
#</div>
#<p>Find the least value of $n$ for which $p(n)$ is divisible by one million.</p>

#it was not possible to use meomization directly on this piece of code
#the nested for loop can not be modified using a cache dictionary
#def sol2(targetModulo):
#	n=1
#	while(True):
#		partitions=[0]*(n+1)
#		partitions[0]=1
#	
#		for coin in range(1,n+1):
#			for i in range(coin,n+1):
#				partitions[i]+=partitions[i-coin]

#		if(partitions[n]%targetModulo==0):
#			return n
#		else:
#			n+=1
#targetModulo=1000000
#print(sol2(targetModulo))

#it is much more efficient to calculate pentagon numbers and use a yield statement to save memory
#https://en.m.wikipedia.org/wiki/Pentagonal_number_theorem
def pentagonal(N):
    a=1
    b=2
    delta=4
    sgn=1
    while(a<=N):
        yield sgn, a
        a+=delta
        if(b<=N):
            yield sgn, b
            b+=delta+1
        delta+=3
        sgn=-sgn

def sol(targetModulo):
	P={}
	P[0]=1
	n=0
	while(P[n]!=0):
	    n+=1
	    P[n]=0
	    for sgn, g in pentagonal(n):
	        P[n]+=sgn*P[n-g]
	        P[n]%=targetModulo
	return n

targetModulo=10**6
print(sol(targetModulo))