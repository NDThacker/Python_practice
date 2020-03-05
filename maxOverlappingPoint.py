import sys
import collections

tests = int(input())

while(tests > 0):
	size = int(input())
	inEvents = list(map(int, input().split()))
	outEvents = list(map(int, input().split()))
	inC = collections.Counter(inEvents)
	oC = collections.Counter(outEvents)
	inEvents = set(inEvents)
	outEvents = set(outEvents)
	totalEs = inEvents.union(outEvents)
	totalEs = list(totalEs)
	totalEs.sort()
	mGuest = 0
	guestCur = 0
	mTime = 0
	for event in totalEs:
		if(event in inC.keys()):
			guestCur += inC[event]
		if(guestCur > mGuest):
			mGuest = guestCur
			mTime = event
		if(event in oC.keys()):
			guestCur -= oC[event]
	print(mGuest, mTime)
	tests -= 1
