#<p>Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.</p>
#<div class="center">
#<img src="resources/images/0068_1.png?1678992052" class="dark_img" alt=""><br></div>
#<p>Working <b>clockwise</b>, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.</p>
#<p>It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.</p>
#<div class="center">
#<table width="400" cellspacing="0" cellpadding="0"><tr><td width="100"><b>Total</b></td><td width="300"><b>Solution Set</b></td>
#</tr><tr><td>9</td><td>4,2,3; 5,3,1; 6,1,2</td>
#</tr><tr><td>9</td><td>4,3,2; 6,2,1; 5,1,3</td>
#</tr><tr><td>10</td><td>2,3,5; 4,5,1; 6,1,3</td>
#</tr><tr><td>10</td><td>2,5,3; 6,3,1; 4,1,5</td>
#</tr><tr><td>11</td><td>1,4,6; 3,6,2; 5,2,4</td>
#</tr><tr><td>11</td><td>1,6,4; 5,4,2; 3,2,6</td>
#</tr><tr><td>12</td><td>1,5,6; 2,6,4; 3,4,5</td>
#</tr><tr><td>12</td><td>1,6,5; 3,5,4; 2,4,6</td>
#</tr></table></div>
#<p>By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.</p>
#<p>Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum <b>16-digit</b> string for a "magic" 5-gon ring?</p>
#<div class="center">
#<img src="resources/images/0068_2.png?1678992052" class="dark_img" alt=""><br></div>

#README: in order to be able so solve this challenge, I started by solving the 3-gong ring problem, then extended it to the 5-gong problem

#build 3-gong ring from numbers using tuples
def extractSequence3(a, b, c, d, e, f):
	#consider numbers on the edges - gongs
	gongs = {a: 0, d: 1, f: 2}
	#find smallest gong
	minGong = gongs[min(gongs.keys())]
	# print(gongs, minGong)
	nums = [(a, b, c), (d, c, e), (f, e, b)]
	#sort branches
	nums = nums[minGong:] + nums[:minGong]
	res = ''
	for num_tup in nums:
		for n in num_tup:
			res += str(n)
	return res

def extractSequence5(a, b, c, d, e, f, g, h, i, j):
	gongs = {a: 0, d: 1, f: 2, h: 3, j: 4}
	minGong = gongs[min(gongs.keys())]
	nums = [(a, b, c), (d, c, e), (f, e, g), (h, g, i), (j, i, b)]
	nums = nums[minGong:] + nums[:minGong]
	res = ''
	for num_tup in nums:
		for n in num_tup:
			res += str(n)
	return res

# 3-gong ring
def threeGongSol(targetLength):
	numbers = [1, 2, 3, 4, 5, 6]
	sol = []
	for a in numbers:
		# duplicate and remove a
		numbersB = numbers[:]
		numbersB.remove(a)
		for b in numbersB:
			# duplicate and remove b
			numbersC = numbersB[:]
			numbersC.remove(b)
			for c in numbersC:
				# calc first line
				lineValue = a + b + c
				# duplicate and remove c
				numbersD = numbersC[:]
				numbersD.remove(c)
				for d in numbersD:
					# duplicate and remove d
					numbersE = numbersD[:]
					numbersE.remove(d)
					# calc e (see image)
					e = lineValue - c - d
					if e in numbersE:
						# duplicate and remove e
						numbersF = numbersE[:]
						numbersF.remove(e)
						# calc f
						f = lineValue - e - b
						# check if f is ok
						if f in numbersF:
							# get gong ring string
							temp = extractSequence3(a, b, c, d, e, f)
							sol.append(temp)

	print("3-gong ring sol:", max([int(x) if len(x) == targetLength else 0 for x in sol]))

#5-gong ring
def fiveGongSol(targetLength):
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	sol = []
	for a in numbers:
		numbersB = numbers[:]
		numbersB.remove(a)
		for b in numbersB:
			numbersC = numbersB[:]
			numbersC.remove(b)
			for c in numbersC:
				lineValue = a + b + c
				numbersD = numbersC[:]
				numbersD.remove(c)
				for d in numbersD:
					numbersE = numbersD[:]
					numbersE.remove(d)
					e = lineValue - c - d
					if e in numbersE:
						numbersF = numbersE[:]
						numbersF.remove(e)
						for f in numbersF:
							numbersG = numbersF[:]
							numbersG.remove(f)
							g = lineValue - e - f
							if g in numbersG:
								numbersH = numbersG[:]
								numbersH.remove(g)
								for h in numbersH:
									numbersI = numbersH[:]
									numbersI.remove(h)
									i = lineValue - g - h
									if i in numbersI:
										j = lineValue - i - b
										numbersJ = numbersI[:]
										numbersJ.remove(i)
										if j in numbersJ:
											s = extractSequence5(a, b, c, d, e, f, g, h, i, j)
											sol.append(s)

	print("5-gong ring sol:", max([int(x) if len(x) == targetLength else 0 for x in sol]))

threeGongSol(9)
fiveGongSol(16)