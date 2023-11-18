#<p>In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:</p>
#<ul><li><b>High Card</b>: Highest value card.</li>
#<li><b>One Pair</b>: Two cards of the same value.</li>
#<li><b>Two Pairs</b>: Two different pairs.</li>
#<li><b>Three of a Kind</b>: Three cards of the same value.</li>
#<li><b>Straight</b>: All cards are consecutive values.</li>
#<li><b>Flush</b>: All cards of the same suit.</li>
#<li><b>Full House</b>: Three of a kind and a pair.</li>
#<li><b>Four of a Kind</b>: Four cards of the same value.</li>
#<li><b>Straight Flush</b>: All cards are consecutive values of same suit.</li>
#<li><b>Royal Flush</b>: Ten, Jack, Queen, King, Ace, in same suit.</li>
#</ul><p>The cards are valued in the order:<br>2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.</p>
#<p>If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.</p>
#<p>Consider the following five hands dealt to two players:</p>
#<div class="center">
#<table><tr><td><b>Hand</b></td><td> </td><td><b>Player 1</b></td><td> </td><td><b>Player 2</b></td><td> </td><td><b>Winner</b></td>
#</tr><tr><td><b>1</b></td><td> </td><td>5H 5C 6S 7S KD<br><div class="smaller">Pair of Fives</div></td><td> </td><td>2C 3S 8S 8D TD<br><div class="smaller">Pair of Eights</div></td><td> </td><td>Player 2</td>
#</tr><tr><td><b>2</b></td><td> </td><td>5D 8C 9S JS AC<br><div class="smaller">Highest card Ace</div></td><td> </td><td>2C 5C 7D 8S QH<br><div class="smaller">Highest card Queen</div></td><td> </td><td>Player 1</td>
#</tr><tr><td><b>3</b></td><td> </td><td>2D 9C AS AH AC<br><div class="smaller">Three Aces</div></td><td> </td><td>3D 6D 7D TD QD<br><div class="smaller">Flush  with Diamonds</div></td><td> </td><td>Player 2</td>
#</tr><tr><td><b>4</b></td><td> </td><td>4D 6S 9H QH QC<br><div class="smaller">Pair of Queens<br>Highest card Nine</div></td><td> </td><td>3D 6D 7H QD QS<br><div class="smaller">Pair of Queens<br>Highest card Seven</div></td><td> </td><td>Player 1</td>
#</tr><tr><td><b>5</b></td><td> </td><td>2H 2D 4C 4D 4S<br><div class="smaller">Full House<br>With Three Fours</div></td><td> </td><td>3C 3D 3S 9S 9D<br><div class="smaller">Full House<br>with Three Threes</div></td><td> </td><td>Player 1</td>
#</tr></table></div>
#<p>The file, <a href="resources/documents/0054_poker.txt">poker.txt</a>, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.</p>
#<p>How many hands does Player 1 win?</p>
from enum import Enum
from collections import Counter
	
class combs(Enum):
	NONE=0
	HIGHCARD=1
	ONEPAIR=2
	TWOPAIRS=3
	THREEOAK=4
	STRAIGHT=5
	FLUSH=6
	FULLHOUSE=7
	FOUROAK=8
	STRAIGHTFLUSH=9
	ROYALFLUSH=10

cardsNames=["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
seeds=["C","S","H","D"]

def convertToNumVal(card):
	if(card=="A"):
		return 14
	elif(card=="K"):
		return 13		
	elif(card=="Q"):
		return 12
	elif(card=="J"):
		return 11
	elif(card=="T"):
		return 10
	return int(card)

def findHighestCard(hand):
	m=0
	for h in range(len(hand)):
		if(hand[h][0]=="A"):
			return combs.HIGHCARD,14, None	
		elif(hand[h][0]=="K"):
			if(13>m):
			     m=13
		elif(hand[h][0]=="Q"):
			if(12>m):
			     m=12
		elif(hand[h][0]=="J"):
			if(11>m):
			     m=11
		elif(hand[h][0]=="T"):
			if(10 >m):
			     m=10
		elif(int(hand[h][0])>m):
			m=int(hand[h][0])
	return combs.HIGHCARD,m, None	
	
def findPairs(hand):
    tmpHand=[]
    for h in range(len(hand)):
    	tmpHand.append(hand[h][0])
    count = list(Counter(tmpHand)-Counter(set(tmpHand)))
    #no pairs
    if(len(count)==0):
    	return combs.NONE, None, None
    #pair
    elif(len(count)==1):
    	return combs.ONEPAIR,  convertToNumVal(count[0]), None
    #two pairs
    count[0]=convertToNumVal(count[0])
    count[1]=convertToNumVal(count[1])
    count=sorted(count)
    return combs.TWOPAIRS,  count[1], count[0]
    
def find3oak(hand):
	tmpHand=[]
	for h in range(len(hand)):
	   tmpHand.append(hand[h][0])
	count = (Counter(tmpHand)-Counter(set(tmpHand)))
	if(count):
		if(count[list(count)[0]]==2):
		   return combs.THREEOAK, convertToNumVal (list(count)[0]), None
	return combs.NONE, None, None
	  
def findStraight(hand):
	scores={14: "A", 13: "K", 12: "Q", 11: "J", 10: "T", 9: "9",
           8: "8", 7: "7", 6: "6", 5: "5", 4: "4", 3: "3", 2: "2", 1: "1"}
           
	tmp, hcVal, tmp2=findHighestCard(hand)
	tmpHand=[]
	for h in range(len(hand)):
	   tmpHand.append(hand[h][0])
	
	if(scores[hcVal-1] in tmpHand):
	       if(scores[hcVal-2] in tmpHand):
	       	if(scores[hcVal-3] in tmpHand):
	       		if(scores[hcVal-4] in tmpHand):
	       			return combs.STRAIGHT, hcVal, None
	return combs.NONE, None, None	
	
def findFlush(hand):
    tmpHand=[]
    for h in range(len(hand)):
    	tmpHand.append(hand[h][1])
    if(len(set(tmpHand))==1):
    	return combs.FLUSH, None, None	
    return combs.NONE, None, None	

def findFullHouse(hand):
    comb, card, temp = findPairs(hand)
    comb2, card2, temp2 = find3oak(hand)
    #3oak is seen as 2 pairs by findPairs
    if(comb==combs.TWOPAIRS and comb2==combs.THREEOAK):
        return combs.FULLHOUSE, card2, card
    return combs.NONE, None, None
    
def find4oak(hand):
    tmpHand=[]
    for h in range(len(hand)):
    	tmpHand.append(hand[h][0])
    count = (Counter(tmpHand)-Counter(set(tmpHand)))
    if(count):
	    if(count[list(count)[0]]==3):
	    	return combs.FOUROAK, convertToNumVal (list(count)[0]), None
    return combs.NONE, None, None
    
def findStraightFlush(hand):
    comb, tmp, tmp2=findFlush(hand)
    comb2, card, tmp3=findStraight(hand)
    if(comb==combs.FLUSH and comb2==combs.STRAIGHT):
    	return combs.STRAIGHTFLUSH, card, None
    return combs.NONE, None, None
    
def findRoyalFlush(hand):
	tmpHand=[]
	tmpHand2=[]
	for h in range(len(hand)):
		tmpHand.append(hand[h][0])
		tmpHand2.append(hand[h][1])
	if(set(['T', 'J', 'Q', 'K', 'A'])==set(tmpHand) and len(set(tmpHand2))==1):
		return combs.ROYALFLUSH, None, None
	return combs.NONE, None, None
	 
def playerHand(hand):
	comb, card1, card2=findRoyalFlush(hand)
	if(comb!=combs.NONE):
		return comb, card1, card2
	comb, card1, card2=findStraightFlush(hand)
	if(comb!=combs.NONE):
		return comb, card1, card2
	comb, card1, card2=find4oak(hand)
	if(comb!=combs.NONE):
		return comb, card1, card2
	comb, card1, card2=findFullHouse(hand)
	if(comb!=combs.NONE):
		return comb, card1, card2
	comb, card1, card2=findFlush(hand)
	if(comb!=combs.NONE):
		return comb, card1, card2
	comb, card1, card2=findStraight(hand)
	if(comb!=combs.NONE):
		return comb, card1, card2
	comb, card1, card2=find3oak(hand)
	if(comb!=combs.NONE):
		return comb, card1, card2
	comb, card1, card2=findPairs(hand)
	if(comb!=combs.NONE):
		return comb, card1, card2
	comb, card1, card2=findHighestCard(hand)
	if(comb!=combs.NONE):
		return comb, card1, card2

#tests	
#testHand=["8C","TS","KC","9H","4S"]
#print(findHighestCard(testHand))
#testHand=["3D","9D","7D","2C","9C"]
#print(findHighestCard(testHand))
#testHand=["5D","6D","5D","8C","9C"]
#print(findPairs(testHand))
#testHand=["5D","AD","5D","AC","9C"]
#print(findPairs(testHand))
#testHand=["5D","6D","5D","5C","9C"]
#print(find3oak(testHand))
#testHand=["5D","6D","5D","5C","9C"]
#print(findStraight(testHand))
#testHand=["5D","6D","7D","8C","9C"]
#print(findStraight(testHand))
#testHand=["8D","9D","TD","JC","QC"]
#print(findStraight(testHand))
#testHand=["3D","9D","TD","JC","QC"]
#print(findFlush(testHand))
#testHand=["4D","9D","TD","JD","QD"]
#print(findFlush(testHand))
#testHand=["3D","3C","TD","JC","QC"]
#print(findFullHouse(testHand))
#testHand=["3D","9D","3D","9D","3D"]
#print(findFullHouse(testHand))
#testHand=["3D","3C","TD","JC","QC"]
#print(find4oak(testHand))
#testHand=["AD","AD","AD","AD","3D"]
#print(find4oak(testHand))
#testHand=["3D","4C","5D","6C","7D"]
#print(findStraightFlush(testHand))
#testHand=["3D","4D","5D","6D","7D"]
#print(findStraightFlush(testHand))
#testHand=["3D","4C","5D","6C","7D"]
#print(findRoyalFlush(testHand))
#testHand=["TD","QD","AD","KD","JD"]
#print(findRoyalFlush(testHand))
#print("______")

with(open("ex54_input.txt", "r") as file):
    lines = file.readlines()

p1 = []
p2 = []
for line in lines:
    elements = line.split()
    p1.append(elements[:5])
    p2.append(elements[5:])

count1=0
for i in range(len(p1)):
	comb1, card11, card12=playerHand(p1[i])
	comb2, card21, card22=playerHand(p2[i])
	if(comb1.value>comb2.value):
		count1+=1
	elif(comb1.value==comb2.value):
		if(card11>card21):
			count1+=1
		
print(count1)
