import sys
tests = int(input())
while(tests > 0):
	seqL = list()
	seqL.append(0)

	occurredL = list()
	indexer = dict()
	counter = dict()
	n = int(input())

	for ind in range(n):
		cur = seqL[-1]
		if(cur in occurredL):
			seqL.append(ind + 1 - indexer[cur])
			indexer[cur] = ind+1
		else:
			seqL.append(0)
			occurredL.append(cur)
			indexer[cur] = ind+1
		counter[cur] = counter.get(cur, 0) + 1

	#print(*seqL)
	print(counter[seqL[n-1]])
	tests -= 1