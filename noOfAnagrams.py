

def checkAna(ind, size, fStr, tList):
	fInd = ind
	while (ind < fInd + size):
		if(fStr[ind] in tList):
			tList.remove(fStr[ind])
		else:
			return 0
		ind +=1
	return -1

noT = int(input())
while(noT):
	fStr = list(input())
	aStr = list(input())
	aCounter = 0
	fSize = len(fStr)
	aSize = len(aStr)
	ind = 0
	while(ind + aSize -1  < fSize):
		tList = list(aStr)
		if(checkAna(ind, aSize, fStr, tList) == -1): 
			aCounter += 1
		ind += 1
	print(aCounter)
	noT -=1    