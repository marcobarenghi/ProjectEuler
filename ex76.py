#<p>It is possible to write five as a sum in exactly six different ways:</p>
#\begin{align}
#&amp;4 + 1\\
#&amp;3 + 2\\
#&amp;3 + 1 + 1\\
#&amp;2 + 2 + 1\\
#&amp;2 + 1 + 1 + 1\\
#&amp;1 + 1 + 1 + 1 + 1
#\end{align}
#<p>How many different ways can one hundred be written as a sum of at least two positive integers?</p>

def sol(nTarget):
    sumCombinations=[0]*(nTarget+1)
    sumCombinations[0]=1
    for i in range(1, nTarget):
        for j in range(i, nTarget+1):
            sumCombinations[j]+=sumCombinations[j-i]
            #the Number of ways to sum n is given by the Number of ways to sum i and (j-i), for all combs of i and j
    return sumCombinations[nTarget]

nTarget=100
#for i in range(2,nTarget+1):
#	print(i,sol(i))
print(sol(nTarget))