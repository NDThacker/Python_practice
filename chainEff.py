import sys
from collections import Counter

tests = int(input())

while (tests > 0):
	size = int(input())
	inArr = [int(x) for x in input().split()]
	freqDist = Counter(inArr)

	print(size - freqDist.most_common()[0][1])
	tests -= 1
