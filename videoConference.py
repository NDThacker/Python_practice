import sys


def notInAny(probe, sSet):
	res = False
	for ele in sSet:
		if(ele.find(probe) != -1):
			res = True
			break
	return res

joinees = int(input())
names = dict()
counter = dict()

while (joinees > 0):
	query = input()

	if(query in counter.keys()):
		counter[query] += 1
		print(query + " " + str(counter[query]))
	else:
		pats = ''
		setC = names.get(query[0], set())
		counter[query] = 1
		if(len(setC) > 0):
			ind = 2
			while (pats != query):
				pats = query[:ind]
				if(not(notInAny(pats, setC))):
					setC.add(pats)
					break
				ind += 1
		else:
			pats = query[0]
		setC.add(query)
		names[query[0]] = setC
		print(pats)
	joinees -= 1
				


