#<p class="small_notice">NOTE: This problem is a more challenging version of <a href="problem=81">Problem 81</a>.</p>
#<p>The minimal path sum in the $5$ by $5$ matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to $994$.</p>
#<div class="center">
#$$
#\begin{pmatrix}
#131 &amp; 673 &amp; \color{red}{234} &amp; \color{red}{103} &amp; \color{red}{18}\\
#\color{red}{201} &amp; \color{red}{96} &amp; \color{red}{342} &amp; 965 &amp; 150\\
#630 &amp; 803 &amp; 746 &amp; 422 &amp; 111\\
#537 &amp; 699 &amp; 497 &amp; 121 &amp; 956\\
#805 &amp; 732 &amp; 524 &amp; 37 &amp; 331
#\end{pmatrix}
#$$
#</div>
#<p>Find the minimal path sum from the left column to the right column in <a href="resources/documents/0082_matrix.txt">matrix.txt</a> (right click and "Save Link/Target As..."), a 31K text file containing an $80$ by $80$ matrix.</p>

#find min path to next line, given x and y
def minPath(x, y, m,solM ):
	dim=len(m)
	sums=[]
	#up
	sumUp=0 
	for up in range(x-1, -1, -1):
		#calc path value
		sums.append(sumUp+m[up][y]+solM[up][y-1])
		sumUp+=m[up][y] 
	#down
	sumDown=0
	for down in range(x+1, dim):
		#calc path value
		sums.append(sumDown+m[down][y]+solM[down][y-1])
		sumDown+=m[down][y]
	return min(sums) 

def sol(m):
	dim=len(m)
	solM=[[0]*dim for i in range(dim)]
	#initialize first column
	for x in range(dim):
		solM[x][0]=m[x][0]
		
	for y in range(1, dim):  # We start at the second column, and go through the matrix
		for x in range(dim):
			#cell value=value of the matrix + either the cell to take left or all the value of a different path, found by minPath
			solM[x][y]+=(m[x][y]+min(solM[x][y-1], minPath(x, y, m, solM)))
	#return min of last column
	return min([solM[x][dim-1] for x in range(0, dim)])
	
f=open('ex82_input.txt', 'r')
matrix=[]
#	matrix=[[131, 673, 234, 103, 18],
#			  [201, 96, 342, 965, 150],
#			  [630, 803, 746, 422, 111],
#			  [537, 699, 497, 121, 956],
#			  [805, 732, 524, 37, 331]]
for line in f:
	matrix.append([int(r) for r in line.split(',')])	
f.close()
print(sol(matrix))