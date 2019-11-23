# def maxDistance(arr, n):
# 	# Code here
# 	elements = set(arr)
# 	distDict = dict()
# 	for ele in elements:
# 		ind = 0
# 		while (ind < n):
# 			if(arr[ind] == ele):
# 				distList = distDict.get(ele, [])
# 				distList.append(ind)
# 				distDict[ele] = distList
# 			ind += 1
# 	maxDist = 0
# 	for ele in elements:
# 		distList = distDict.get(ele, [])
# 		if(len(distList) > 1 and maxDist < (distList[-1] - distList[0])):
# 			maxDist = distList[-1] - distList[0]
# 	return maxDist

def maxDistance(arr, n):
	elements = set(arr)
	maxDist = 0
	if (len(arr) == 0):
		return 0
	for ele in elements:
		fInd = arr.index(ele)
		arr.reverse()
		lInd = n - 1 - arr.index(ele)
		if(lInd - fInd > maxDist):
			maxDist = lInd - fInd
	return maxDist


print(maxDistance([1, 2, 3, 1, 2, 3, 3], 7))