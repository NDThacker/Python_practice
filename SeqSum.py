import sys
testcases = int(input())
totSum, length, inpNums = 0, 0, []

def findSum(inpNums, curI, curSum, totSum, resultSet):
	if(curI >= len(inpNums)):
		return resultSet
	if(curSum == totSum):
		return resultSet
	else:
		if(curSum + inpNums[curI] == totSum):
			resultSet.append(inpNums[curI])
			return resultSet
		resultSet.append(inpNums[curI])
		resultSet = findSum(inpNums, curI + 1, curSum + inpNums[curI], totSum, resultSet)
		if(not(sum(resultSet) == totSum)):
			resultSet.pop()
			resultSet = findSum(inpNums, curI + 1, curSum, totSum, resultSet)
	return resultSet


while(testcases > 0):
	totSum = int(input()) - 1
	length = int(input())
	inpNums = [(int(x) + 1) for x in input().split()]
	inpNums.sort(reverse = True)
	resultSet = findSum(inpNums, 0, 0, totSum, [])
	if(len(resultSet) == 0):
		print(-1)
		testcases -= 1
		continue
	rs2 = [x - 1 for x in resultSet]
	print(*rs2, sep=" ")
	testcases -= 1