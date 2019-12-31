import sys

def sMakeChange(ind, curS, coinsL, coins, change):
	
	rt = 0
	count1 = 0
	count3 = 0
	if(change == (coinsL[ind] + curS)):
		# print("caught", end = ' ')
		rt = 1
	# print("called " + str(ind) + " " + str(curS))
	if(coinsL[ind] + curS < change):
		# print("self " + str(ind) + " " + str(curS))
		count3 = sMakeChange(ind, curS + coinsL[ind], coinsL, coins, change)
	if(coinsL[ind] + curS < change and ind + 1 < coins):
		# print("took and then " + str(ind) + " " + str(curS))
		count1 = makeChange(ind + 1, curS + coinsL[ind], coinsL, coins, change)
	return count1 + count3 + rt



def makeChange(ind, curS, coinsL, coins, change):
	
	rt = 0
	count1 = 0
	count2 = 0
	count3 = 0
	if(change == (coinsL[ind] + curS)):
		# print("caught", end = ' ')
		rt = 1
	# print("called " + str(ind) + " " + str(curS))
	if(coinsL[ind] + curS < change):
		# print("self " + str(ind) + " " + str(curS))
		count3 = sMakeChange(ind, curS + coinsL[ind], coinsL, coins, change)
	if(coinsL[ind] + curS < change and ind + 1 < coins):
		# print("took and then " + str(ind) + " " + str(curS))
		count1 = makeChange(ind + 1, curS + coinsL[ind], coinsL, coins, change)
	if(ind + 1 < coins):
		# print("left out and then " + str(ind) + " " + str(curS))
		count2 = makeChange(ind + 1, curS, coinsL, coins, change)
	return count1 + count2 + count3 + rt

change, coins = [int(x) for x in input().split()]
coinsL = [int(x) for x in input().split()]
print(makeChange(0, 0, coinsL, coins, change))