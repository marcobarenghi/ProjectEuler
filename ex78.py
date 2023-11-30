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

def sol(targetModulo):
	n=1
	while(True):
		#should use meomization on partitions
		partitions=[0]*(n+1)
		partitions[0]=1

	#modify for loop accordingly
		for coin in range(1,n+1):
			for i in range(coin,n+1):
				partitions[i]+=partitions[i-coin]
		
		print(partitions)
		if(partitions[n]%targetModulo==0):
			return n
		else:
			n+=1

targetModulo=10
print(sol(nMax))