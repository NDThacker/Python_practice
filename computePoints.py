import sys

tests = int(input())
while tests > 0:
	size = int(input())
	
	inL = [int(x) for x in input().split()]
	if(size == 1)
		return inL[0]
	inL.sort()
	
	health = 1
	exp = 0
	minE = sum(inL)
	tot = minE
	maxE = 0
	for entry in inL:
		health += 1
		minE = (tot - entry) * health
		tot -= entry
		if(maxE < minE):
			maxE = minE
	print(maxE)
	tests -= 1