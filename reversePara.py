import sys

noL = int(input())
paragraph = ''

while(noL > 0):
	paragraph += input()
	noL -= 1

for c in ['.',',',';',':','\'']:
	paragraph = paragraph.replace(c, '')

paragraph = paragraph.replace('  ', ' ')
listOfW = paragraph.split()
listOfW.reverse()

print(*listOfW)



