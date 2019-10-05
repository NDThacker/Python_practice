stringnum = ["10", "20", "13", "12345"]

stringnum = sorted(stringnum, key=lambda x: len(x))
stringnum = sorted(stringnum)

print(stringnum)