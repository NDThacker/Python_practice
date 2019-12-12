import sys
from collections import Counter

def calMaxK(ch, count, inpStr):
	indc = inpStr.find(ch)
	dist = len(inpStr) + 1
	for _ in range(count-1):
		indl = inpStr.find(ch, indc+1)
		if(indl - indc < dist):
			dist = indl - indc
	
	return len(inpStr) - dist


tests = int(input())
maxK = 0
while (tests > 0):
	maxK = 0
	size = int(input())
	inpStr = input()
	freqDist = Counter(inpStr)
	noSol = False
	for entry, freq in freqDist.most_common():
		if(freq == 1):
			break
		res = calMaxK(entry, freq, inpStr)
		if(res > maxK):
			maxK = res
	print(maxK)
	tests -= 1
		
		
