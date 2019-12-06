import sys

def updateRes(nodeQ, res, edgeMat, node, nodes, visited):
	visited.append(node)
	for adjN in edgeMat[node-1]:
		if(res[adjN] != -1):
			if(res[node-1] + 1 < res[adjN]):
				res[adjN] = res[node-1] + 1
		else:
			res[adjN] = res[node-1] + 1
		if((adjN+1) not in visited):
			nodeQ.append(adjN + 1)

nodes, edges = [int(x) for x in input().split()]

edgeMat = [[] for _ in range(nodes)]
for _ in range(edges):
	n1, n2 = [int(x) for x in input().split()]
	edgeMat[n1-1].append(n2-1)
	edgeMat[n2-1].append(n1-1)

start, end = [int(x) for x in input().split()]


nodeQ = []
nodeQ.append(start)
res = [-1 for _ in range(nodes)]
res[start-1] = 0
visited = []
while (len(nodeQ) > 0):
	node = nodeQ[0]
	#print(node)
	nodeQ.remove(nodeQ[0])
	updateRes(nodeQ, res, edgeMat, node, nodes, visited)
if(res[end-1] == -1):
	print(0)
else:
	print(res[end-1])
	
