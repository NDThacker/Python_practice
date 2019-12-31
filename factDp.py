import sys

inp = int(input())

def factDp(numF, dpDict):
	if(dpDict.get(numF, 0) != 0):
			return dpDict[numF]
	dpDict[numF] = factDp(numF - 1, dpDict) * numF
	return dpDict[numF]

dpDict = {}
dpDict[1] = 1
dpDict[0] = 1
dpDict[2] = 2
print(factDp(inp, dpDict))
