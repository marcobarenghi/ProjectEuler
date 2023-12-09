#<p>In the game, <strong>Monopoly</strong>, the standard board is set up in the following way:</p>
#<div class="center">
#<img src="resources/images/0084_monopoly_board.png?1678992052" alt="0084_monopoly_board.png">
#</div>
#<p>A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.</p>
#<p>In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.</p>
#<p>At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.</p>
#<ul><li>Community Chest (2/16 cards):
#<ol><li>Advance to GO</li>
#<li>Go to JAIL</li>
#</ol></li>
#<li>Chance (10/16 cards):
#<ol><li>Advance to GO</li>
#<li>Go to JAIL</li>
#<li>Go to C1</li>
#<li>Go to E3</li>
#<li>Go to H2</li>
#<li>Go to R1</li>
#<li>Go to next R (railway company)</li>
#<li>Go to next R</li>
#<li>Go to next U (utility company)</li>
#<li>Go back 3 squares.</li>
#</ol></li>
#</ul><p>The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final square that the player finishes at on each roll that we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.</p>
#<p>By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.</p>
#<p>Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.</p>
#<p>If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.</p>
import random
random.seed(43)

squares=["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3", "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3", "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3", "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]
nSquares=len(squares)
squaresIDs={s: i for i, s in enumerate(squares)}
squaresCounts=[0]*nSquares

#railways
#RC={"R1":5,"R2":15,"R3":25,"R4":35}
RC=[5,15,25,35]
#utilities
#UC={"U1":13,"U2":29}
UC=[12,28]
#CC
CC=["CC1","CC2","CC3"]
#CH
CH=["CH1","CH2","CH3"]

#CC and CH cards
nRandomCards=16
cardsCC=["GO", "JAIL"]
for i in range(nRandomCards-len(cardsCC)):
	cardsCC.append("NONE")
cardsCH=["GO", "JAIL", "C1","E3","H2", "R1", "NEXTR","NEXTR","NEXTU","BACK3"]
for i in range(nRandomCards-len(cardsCH)):
	cardsCH.append("NONE")
random.shuffle(cardsCC)
random.shuffle(cardsCH)

def sol(dice, nRolls):
	pos=0
	currCCCard=0
	currCHCard=0
	activeDoubles=0
	count=[0]*len(squares)
	for n in range(nRolls):
		a,b=random.randint(1,dice),random.randint(1,dice)
		pos=(pos+a+b)%nSquares
		#handle double rule
		if(a==b):
			activeDoubles+=1
		else:
			activeDoubles=0
		
		#jail cases
		if(activeDoubles==3):
			pos=squaresIDs["JAIL"]	
		elif(squares[pos]=="G2J"):
			pos=squaresIDs["JAIL"]
	
		#CH cases
		elif(squares[pos] in CH):
			if(cardsCH[currCHCard]=="NONE"):
				pass
			elif(cardsCH[currCHCard]=="NEXTR"):
				found=False
				for i in range(len(RC)-1):
					if(pos<RC[i+1] and pos>RC[i]):
						found=True
						pos=RC[i+1]
						break		
				if(not found):
					pos=RC[0]
			elif(cardsCH[currCHCard]=="NEXTU"):
				if(pos<UC[1] and pos>UC[0]):
					pos=UC[1]
				else:
					pos=UC[0]
			elif(cardsCH[currCHCard]=="BACK3"):
				pos=(pos-3)%nSquares
			else:
				pos=squaresIDs[cardsCH[currCHCard]]
			currCHCard=(currCHCard+1)%nRandomCards
			
		#CC cases	
		elif(squares[pos] in CC):
			if(cardsCC[currCCCard]!="NONE"):
				pos=squaresIDs[cardsCC[currCCCard]]
			currCCCard=(currCCCard+1)%nRandomCards
			
		#update counter
		count[pos]+=1

	#create string of IDs
	bestN=3
	string=""
	for i in range(bestN):
		best=count.index(max(count))
		count[best]=-1
		if(len(str(best))==1):
			string+="0"+str(best)
		else:
			string+=str(best)

	return string
	
print("6-sides dice:", sol(6,10**6))
print("4-sided dice:", sol(4,10**6))