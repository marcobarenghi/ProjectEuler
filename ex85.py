#<p>By counting carefully it can be seen that a rectangular grid measuring $3$ by $2$ contains eighteen rectangles:</p>
#<div class="center">
#<img src="resources/images/0085.png?1678992052" class="dark_img" alt=""></div>
#<p>Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.</p>

def nRects(height, width):
    n=0
    for h in range(1, height+1):
        for w in range(1, width+1):
            n+=(height-h+1)*(width-w+1)
    return n
    
nTarget=2*10**6
diff=nTarget
bestArea=0
bX, bY=0,0
#100 found with attempts
for x in range(1,100):
	for y in range(x,100):
		n=nRects(x,y)
		if(abs(n-nTarget)<diff):
			bestArea=x*y
			diff=abs(n-nTarget)
			
print(bestArea)		