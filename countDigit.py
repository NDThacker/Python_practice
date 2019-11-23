def num(arr, n, k):
	# Code here
	kCount = 0
	for number in arr:
		numList = list(str(number))
		print(numList)
		kCount += numList.count(str(k))
	return kCount



print(num([12, 13, 14], 3, 1))