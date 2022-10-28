import sys

def findDiff(intL, size):
	potentDiff = -1
	maxFeq = 0
	freqs = dict()	
	for itr in range(1, size):
		if((intL[itr] - intL[itr-1]) == 0):
			continue
		if((intL[itr] - intL[itr-1]) in freqs.keys()):
			if((intL[itr-1] - intL[itr-2]) == (intL[itr] - intL[itr-1])):
				freqs[(intL[itr] - intL[itr-1])] += 1
		elif((itr - 2 >= 0 and intL[itr-1] - intL[itr-2] > 0) and ((intL[itr-1] - intL[itr-2]) % (intL[itr] - intL[itr-1]) == 0 or (intL[itr] - intL[itr-1]) % (intL[itr-1] - intL[itr-2]) == 0)):
			if((intL[itr-1] - intL[itr-2]) > (intL[itr] - intL[itr-1])):
				freqs[(intL[itr] - intL[itr-1])] = 2
			else:
				freqs[(intL[itr-1] - intL[itr-2])] = 2
		else:
			freqs[(intL[itr] - intL[itr-1])] = 1
	for fKey in freqs.keys():
		# print(maxFeq, potentDiff)
		if(freqs[fKey] > maxFeq):
			maxFeq = freqs[fKey]
			potentDiff = fKey
	return potentDiff		


testcases = int(input())
while(testcases > 0):
	size = int(input())
	intL = [int(x) for x in input().split()]
	intL.sort()
	potentDiff = findDiff(intL, size)
	if(potentDiff == -1):
		print("NO")
		testcases -= 1
		continue
	failures = 0
	itr = 1
	# print(potentDiff)
	while(itr < size):
		if((intL[itr] - intL[0]) % potentDiff != 0):
			failures += 1
		# print(failures)
		if(failures == 2):
			break
		itr += 1
	if(failures == 2):
		print("NO")
	else:
		print("YES")
	testcases -= 1

