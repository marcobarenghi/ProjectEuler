#<p>In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:</p>
#<blockquote>1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).</blockquote>
#<p>It is possible to make £2 in the following way:</p>
#<blockquote>1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p</blockquote>
#<p>How many different ways can £2 be made using any number of coins?</p>
import time

#of course brute force methods could solve this
#recursion can be more efficient
def countWaysRec(target, denoms):
	#if amount is 0 -> comb is ok, count it
	if(target == 0):
		return 1
	#if amount below 0 or no more demos -> comb not ok, quit and do not count
	if(target < 0 or not denoms):
		return 0
	#the key is to subtract the largest denom from the amount and recursively calls itself
	return countWaysRec(target - denoms[0], denoms) + countWaysRec(target, denoms[1:])
	
#dynamic programming uses  array to store already-calculated combinations
def countWaysDyn(target, denom):
    combs = [0] * (target + 1)
    combs[0] = 1  #only one way to make change for 0
    
	#for each denom we find the combination starting from the denom itself to the target value. combs is updated by every denom, accounting for all possible combinations.
    for coin in denom:
        for i in range(coin, target + 1):
            combs[i] += combs[i - coin]
    return combs[target]
  
#quick testing  
#dTest=[5,2,1]
#tTest=1
#nTest=countWays(tTest, dTest)
#print(nTest)
	
#dTest=[10,5,2,1]
#tTest=5
#nTest=countWays(tTest, dTest)
#print(nTest)

denoms=[200, 100, 50, 20, 10, 5, 2, 1]
target=200

start1=time.time()
n=countWaysRec(target, denoms)
end1=time.time()
print(n)

start2=time.time()
n=countWaysDyn(target,denoms)
end2=time.time()
print(n)

#in the end, the dyn approach is much more faster.
#recursive approach performance worsens as the scale of the problem increases.
print("Time Rec/Time Dyn=", int((end1-start1)/(end2-start2)))