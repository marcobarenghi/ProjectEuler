#Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#For example, when the list is sorted into alphabetical order, COLIN, which is worth $3 + 15 + 12 + 9 + 14 = 53$, is the $938$th name in the list. So, COLIN would obtain a score of $938 \times 53 = 49714$.
#What is the total of all the name scores in the file?

with open("ex22_names.txt", "r") as file:
    content = file.read()

# Remove quotation marks and use commas as dividers
names= content.replace('"', '').split(',')
names=sorted(names)

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

totScore=0
for n in range(len(names)):
	#score for each name
	score=0
	for i in range(len(names[n])):
		for l in range(len(letters)):
			if(names[n][i]==letters[l]):
				score+=l+1
				break
	score*=(n+1)
	totScore+=score
print(totScore )