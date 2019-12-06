import sys
l1, l2, l3 = [int(x) for x in input().split()]

vList = dict()


for _ in range(l1+l2+l3):
	idV = int(input())
	vList[idV] = vList.get(idV, 0) + 1

res = []
for ids in vList.keys():
	if(vList[ids] >= 2):
		res.append(ids)

res.sort()
# print("length of final list " + str(len(res)))

for ids in res:
	print(ids)
