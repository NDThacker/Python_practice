import sys


def checkSorted(ls):
	size = len(ls)

	for ind in range(size-1):
		if(ls[ind] > ls[ind+1]):
			return False
	return True

def checkSR(start, end, unsorted):
	#print(start, end)
	dummy = unsorted[:start]
	dummy.append(unsorted[end])
	dummy += unsorted[start+1:end]
	dummy.append(unsorted[start])
	dummy += unsorted[end+1:]

	if(checkSorted(dummy)):
		return 1
	dummy = unsorted[:start]
	dummy2 = unsorted[start:end+1]
	dummy2.reverse()
	dummy += dummy2
	dummy += unsorted[end+1:]

	if(checkSorted(dummy)):
		return 2
	else:
		return -1

size = int(input())

unsorted = [int(x) for x in input().split()]
if(checkSorted(unsorted)):
	print("yes")
	sys.exit(0)
fwd = 0
bwd = size - 1

while(fwd < size - 1 and bwd > 0):
	if(unsorted[fwd] > unsorted[fwd+1] and unsorted[bwd] < unsorted[bwd-1]):
		res = checkSR(fwd, bwd, unsorted)
		oper = ""
		if(res == 1):
			oper = "swap "
		elif(res == 2):
			oper = "reverse "
		else:
			print("no")
			break
		print("yes\n" + oper + str(fwd+1) + " " + str(bwd+1))
		break
	if(unsorted[fwd] > unsorted[fwd+1] and not (unsorted[bwd] < unsorted[bwd-1])):
		bwd -= 1
		continue
	if(not (unsorted[fwd] > unsorted[fwd+1]) and unsorted[bwd] < unsorted[bwd-1]):
		fwd += 1
		continue
	fwd += 1
	bwd -= 1