import sys

tests = int(input())

while (tests > 0):
	size = int(input())
	arr = []
	hashed = {}
	for x in input().split():
		x = int(x)
		arr.append(x)
		hashed[x] = hashed.get(x, 0) + 1
	needed = 0
	count = 0
	for ind in range(size):
		if(arr[ind] % (arr[ind] - 1) == 0):
			needed = arr[ind] // (arr[ind] - 1)
			needi = hashed.get(needed, -1)
			if(needi != -1):
				count += (needi - 1)
	print(count // 2)
	tests -= 1