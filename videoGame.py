import sys

size, mH = [int(x) for x in input().split()]
stacks = [int(x) for x in input().split()]
pointer = 0
crane = 0
choiceL = [int(x) for x in input().split()]

for ch in choiceL:
	if(ch == 2):
		if(pointer < size - 1):
			pointer += 1
	elif(ch == 1):
		if(pointer > 0):
			pointer -= 1
	elif(ch == 3):
		if(stacks[pointer] > 0):
			stacks[pointer] -= 1
			crane += 1
	elif(ch == 4):
		if(crane >= 1):
			if(stacks[pointer] < mH):
				stacks[pointer] += 1
				crane -= 1
	else:
		break

print(*stacks)
print(crane)