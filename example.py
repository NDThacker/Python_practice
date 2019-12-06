import sys

tests = int(input())

symbols = ['!', '#', '$', '%', '&', '*', '@', '^', '~']

while (tests > 0):
    nuts = input()
    bolts = input()
    res = ''
    for sym in symbols:
        #print(sym)
        if((sym in nuts) and (sym in bolts)):
            res += (sym + ' ')
    print(res)
    print(res)
    tests -= 1
    