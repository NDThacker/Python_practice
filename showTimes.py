import sys

def findMaxRev(posCl):

	maxR = -400
	print(posCl)
	for pL in posCl:
		pL = list(pL)
		pL = [int(x) for x in pL]
		pL.sort(reverse = True)
		# print(*pL)
		initR = 100
		curR = 0
		for rs in pL:
			curR += initR * rs
			initR -= 25
		curR -= (100 * (4 - len(pL)))
		if(curR > maxR):
			maxR = curR
	return maxR


def findMaxReq(tableDict, show, exL):
	maxS = ['', 0]
	for aKeys in tableDict:
		# print(tableDict[aKeys])
		if(not(aKeys in exL) and tableDict[aKeys].get(show, 0) > maxS[1]):
			maxS[0] = aKeys
			maxS[1] = tableDict[aKeys][show]
	return maxS


def findSeq(tableDict, seq, show, curDict):
	if(show == 0):
		return [seq]
	exL = []
	nextDict = dict(curDict)
	retL = []
	ret = ''
	# print("Called " + str(show))
	while(True):
		maxS = findMaxReq(tableDict, show, exL)
		if(maxS[1] == 0):
			if(len(exL) == 0):
				ret = findSeq(tableDict, seq, show - 3, curDict)
				if(not(ret[0])):
					return ret
				else:
					retL.extend(ret)
					break
			else:
				return [False, exL[0]]
			break
		# print(*maxS, show)
		if(maxS[0] in curDict.keys()):
			if(maxS[1] <= curDict[maxS[0]]):
				exL.append(maxS[0])
			else:
				retL.extend(findSeq(tableDict, seq, show - 3, curDict))
				return [False, maxS[0]]
		else:
			nextDict[maxS[0]] = show
			ret = findSeq(tableDict, seq + str(maxS[1]), show - 3, nextDict)
			if(not ret[0]):
				if(ret[1] == maxS[0]):
					exL.append(maxS[0])
					del nextDict[maxS[0]]
				else:
					return ret
			else:
				
				retL.extend(ret)
				break
	# print("returned ", end = '')
	# print(*retL)
	return retL

tests = int(input())
totProfit = 0
while tests > 0:
	tableDict = dict()
	tableDict['A'] = dict()
	tableDict['B'] = dict()
	tableDict['C'] = dict()
	tableDict['D'] = dict()

	noR = int(input())
	for _ in range(noR):
		show, number = [x for x in input().split()]
		number = int(number)
		tableDict[show][number] = tableDict[show].get(number, 0) + 1
	possibleCombs = findSeq(tableDict, "", 12, dict())
	# print(*possibleCombs)
	profit = findMaxRev(possibleCombs)
	print(profit)
	totProfit += profit

	tests -= 1
print(totProfit)
