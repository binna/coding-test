import sys
start, end = map(int, sys.stdin.readline().rstrip().split())
notDecimalList = [True for _ in range(1000000)]

notDecimalList[0] = False
for i in range(2, int(1000000 ** 0.5)):
    if notDecimalList[i - 1]:
        for j in range(i + i, 1000000, i):
            notDecimalList[j - 1] = False

for i in range(start, end + 1):
    if i != 0 and notDecimalList[i - 1]:
        print(i)
