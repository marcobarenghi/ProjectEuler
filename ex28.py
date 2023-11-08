#<p>Starting with the number $1$ and moving to the right in a clockwise direction a $5$ by $5$ spiral is formed as follows:</p>
#<p class="monospace center"><span class="red"><b>21</b></span> 22 23 24 <span class="red"><b>25</b></span><br>
#20  <span class="red"><b>7</b></span>  8  <span class="red"><b>9</b></span> 10<br>
#19  6  <span class="red"><b>1</b></span>  2 11<br>
#18  <span class="red"><b>5</b></span>  4  <span class="red"><b>3</b></span> 12<br><span class="red"><b>17</b></span> 16 15 14 <span class="red"><b>13</b></span></p>
#<p>It can be verified that the sum of the numbers on the diagonals is $101$.</p>
#<p>What is the sum of the numbers on the diagonals in a $1001$ by $1001$ spiral formed in the same way?</p>

#this type of spiral Is also known as Ulam spiral.

def spiral(n):
	#generate matrix to be filled
	matrix = [[0] * n for _ in range(n)]

	# current coordinates
	x, y = n // 2, n // 2
	i = 1
	# "fake" initial data
	direction = "down"
	currentDim=-1
	edgeDim=-1

	while (i<=n**2):
		# fill the matrix
		matrix[y][x]=i

		# down ->right + update edge dim
		if(direction=="down"):
			if(currentDim==edgeDim):
				direction="right"
				currentDim=0
				edgeDim+=1
				x+=1
			else:
				currentDim+=1
				y+=1
		
		# right ->up			
		elif(direction=="right"):
			if(currentDim==edgeDim):
				direction="up"
				currentDim=0
				y-=1
			else:
				currentDim+=1
				x+=1
		
		# up ->left + update edge dim				
		elif(direction=="up"):
			if(currentDim==edgeDim):
				direction="left"
				currentDim=0
				edgeDim+=1
				x-=1
			else:
				currentDim+=1
				y-=1
		
		# left ->down				
		elif(direction=="left"):
			if(currentDim==edgeDim):
				direction="down"
				currentDim=0
				y+=1
			else:
				currentDim+=1
				x-=1
		
		#update i		
		i+=1
	return matrix
	
def sumDiagonals(matrix):
	s1=0
	s2=0
	d=len(matrix)
	for i in range(d):
		s1+=matrix[i][i]
		s2+=matrix[i][d-1-i]
	#center must not be counted twice -> subtract 1
	return(s1+s2-1)

#quick test	
d=5
sTest=spiral(d)
print(sumDiagonals(sTest))
	
n=1001
s=spiral(1001)
print(sumDiagonals(s))

