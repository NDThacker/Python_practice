import sys

tests = int(input())

while tests > 0:
	noC, change = [int(x) for x in input().split()]

	denos = [int(x) for x in input().split()]
	denos.sort()
	res = [0 for _ in range(noC)]
	singleC = False
	oneNum = 0
	idx = 0
	for idx in range(noC - 1, -1, -1):
		if(change % denos[idx] != 0):
			singleC = True
			oneNum = change // denos[idx] + 1
			break
	if(singleC):
		res[idx] = oneNum
		print("YES ", end = '')
		print(*res)
		tests -= 1
		continue
	else:
		curSum = change
		divs = 0
		multiC = False
		for idx in range(noC - 1, -1, -1):
			if(curSum % denos[idx] == 0):
				divs = curSum // denos[idx] - 1
				curSum -= (divs * denos[idx])
				res[idx] = divs
			else:
				multiC = True
				divs = curSum // denos[idx] + 1
				res[idx] = divs
				break
		if(multiC):
			print("YES ", end = '')
			print(*res)
		else:
			print("NO")
		tests -= 1