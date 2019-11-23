noT = int(input())

def printRPairs(inpL):
	count = 0
	ind = 0
	leng = len(inpL) - 1
	while (ind < leng):
		if(inpL[ind] == 0 or ind == 0):
			ind += 1
			continue
		ind2 = ind + 1
		while(ind2 < leng+1):
			if(inpL[ind] > inpL[ind2]):
				count += 1
			ind2 += 1
		ind += 1
	return count
		


while (noT > 0):
	size = int(input())
	inpL = [int(x) for x in input().split()]
	multiL = [x*ind for ind, x in enumerate(inpL)]
	print(printRPairs(multiL))
	noT -= 1