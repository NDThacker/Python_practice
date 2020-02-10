import sys

def computePath(diff, maxS, maxJ, ansDict):
	count = 0
	for poss in range(1, maxJ + 1):
		if(diff - poss < 0):
			break
		else:
			count += ansDict[diff - poss]
	return count


inL = list(map(int, input().split()))
maxS = inL[0]
maxJ = inL[1]

ansDict = dict()
ansDict[0] = 1
ansDict[1] = 1
for diff in range(2, maxS):
	ansDict[diff] = computePath(diff, maxS, maxJ, ansDict)
print(ansDict[maxS-1] % (10**9 + 7))

