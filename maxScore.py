import sys

tests = int(input())
subs = 0
sSum = 0
scores = {}
while (tests > 0):
	scores.clear()
	sSum = 0
	subs = int(input())
	for _ in range(subs):
		sub = [int(x) for x in input().split()]

		if (sub[0] <= 8 and scores.get(sub[0], 0) <= sub[1]):
			scores[sub[0]] = sub[1]
	for mScores in scores.keys():
		sSum += scores[mScores]
	print(sSum)
	tests -= 1


