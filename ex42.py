#<p>The $n$<sup>th</sup> term of the sequence of triangle numbers is given by, $t_n = \frac12n(n+1)$; so the first ten triangle numbers are:
#$$1, 3, 6, 10, 15, 21, 28, 36, 45, 55, \dots$$</p>
#<p>By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is $19 + 11 + 25 = 55 = t_{10}$. If the word value is a triangle number then we shall call the word a triangle word.</p>
#<p>Using <a href="resources/documents/0042_words.txt">words.txt</a> (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?</p>
def calcTriangle(n):
	return int((n*(n+1))/2)

with open("ex42_names.txt","r") as file:
    content = file.read()
input = content.split(',')
input = [name.strip('"') for name in input]

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

count=0
for i in range(len(input)):	
	score=0
	for j in range(len(input[i])):		
		for k in range(len(alphabet)):
			if(input[i][j]==alphabet[k]):
				score+=k+1
				break
	n=1
	while(True):
		scoreTmp=calcTriangle(n)
		print(score,scoreTmp)
		if(score==scoreTmp):
			count+=1
			break
		if(scoreTmp>score):
			break
		n+=1

print(count)