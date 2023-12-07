#<p class="small_notice">NOTE: This problem is a significantly more challenging version of <a href="problem=81">Problem 81</a>.</p>
#<p>In the $5$ by $5$ matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to $2297$.</p>
#<div class="center">
#$$
#\begin{pmatrix}
#\color{red}{131} &amp; 673 &amp; \color{red}{234} &amp; \color{red}{103} &amp; \color{red}{18}\\
#\color{red}{201} &amp; \color{red}{96} &amp; \color{red}{342} &amp; 965 &amp; \color{red}{150}\\
#630 &amp; 803 &amp; 746 &amp; \color{red}{422} &amp; \color{red}{111}\\
#537 &amp; 699 &amp; 497 &amp; \color{red}{121} &amp; 956\\
#805 &amp; 732 &amp; 524 &amp; \color{red}{37} &amp; \color{red}{331}
#\end{pmatrix}
#$$
#</div>
#<p>Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in <a href="resources/documents/0083_matrix.txt">matrix.txt</a> (right click and "Save Link/Target As..."), a 31K text file containing an $80$ by $80$ matrix.</p>

#Dijkstra's algorithm finds the shortest path from a specified starting node to all other nodes in a weighted graph. It maintains a set of vertices with known distances and explores neighboring vertices, updating distances if shorter paths are found. Time complexity is O((V + E) log V), where V is the number of vertices and E is the number of edges in the graph.
#Since we have a 2D matrix, the implementation was relatively easier than with a complex graph and performance is quite good.

def dijkstra(m, startV, endV):
    dim=len(m)
    #distances set - initialize
    d={vertex: float('infinity') for vertex in range(dim**2)}
    d[startV]=m[startV//dim][startV%dim]
    visited=set()

    while(len(visited)<dim**2):
       #unvisited vertex with the minimum distance value
        currV=min((vertex for vertex in range(dim**2) if vertex not in visited),key=d.get)
        visited.add(currV)

        row, col=divmod(currV, dim)
		#consider 4 neighbors
        for neighborRow, neighborCol in [
            (row-1, col), (row+1, col),
            (row, col-1), (row, col+1)
        ]:
            #update distance array if min path is found
            if(0<=neighborRow<dim and 0<= neighborCol<dim):
                neighborV=neighborRow*dim+neighborCol        
                w=m[neighborRow][neighborCol]
                if(d[currV]+w<d[neighborV]):
                    d[neighborV]=d[currV]+w
    return d[endV]

f=open('ex83_input.txt', 'r')
#matrix=[[131, 673, 234, 103, 18],
#			  [201, 96, 342, 965, 150],
#			  [630, 803, 746, 422, 111],
#			  [537, 699, 497, 121, 956],
#			  [805, 732, 524, 37, 331]]
matrix=[]
for line in f:
	matrix.append([int(r) for r in line.split(',')])	
f.close()

#top left
startVertex=0
#bottom right
endVertex=len(matrix)**2-1
result=dijkstra(matrix, startVertex, endVertex)
print("Distance from vertex", startVertex, "to end vertex", endVertex, "=", result)