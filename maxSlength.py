import sys

def countUnique(hashed):
	return len(hashed.keys())

def removeAndCountUnique(hashed, start, inStr):
	if(hashed[inStr[start]] == 1):
		del hashed[inStr[start]]
	else:
		hashed[inStr[start]] -= 1
	return [countUnique(hashed), hashed]
tests = int(input())
while(tests > 0):
	inStr = list(input())
	uniEl = int(input())
	size = len(inStr)
	if(len(set(inStr)) < uniEl):
		print(-1)
		tests -= 1
		continue
	hashed = dict()
	start = 0
	stop = 0
	sLength = 0
	maxSStart = 0
	curUni = 1
	hashed[inStr[0]] = 1
	while(stop + 1 < size):
		stop += 1
		if(not(inStr[stop] in hashed.keys())):
			if(curUni >= uniEl):
				hashed[inStr[stop]] = 1
				curUni, hashed = removeAndCountUnique(hashed, start, inStr)
				start += 1
			else:
				hashed[inStr[stop]] = 1
				curUni += 1
		elif(curUni > uniEl):
			hashed[inStr[stop]] += 1
			curUni, hashed = removeAndCountUnique(hashed, start, inStr)
			start += 1
		else:
			hashed[inStr[stop]] += 1
		if(curUni == uniEl and sLength < stop - start + 1):
				sLength = stop - start + 1
				maxSStart = start		
	print(sLength)
	#print(*inStr[maxSStart : maxSStart + sLength])
	tests -= 1
