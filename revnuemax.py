t=int(input())

a=list()
while(t):
	b=int(input())
	a.append(b)
	t-=1
a.sort()
l=list()
j=0
for i in a:
	l.append(i*(len(a)-j))
	j+=1
print(max(l))

