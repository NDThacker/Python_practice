import sys

inL = [int(x) for x in list(input())]

outL = []

size = len(inL) - 1
evens = 0
for ind in range(size, -1, -1):
	if(inL[ind] % 2 == 0):
		evens += 1
	outL.append(evens)
outL.reverse()
print(*outL)
