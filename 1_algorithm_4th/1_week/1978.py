import sys

n = int(input())
data = list(map(int, sys.stdin.readline().rstrip().split()))
result = []


def searchDecimal(targetNum):
    if targetNum == 0 or targetNum == 1:
        return False
    for idx in range(2, targetNum):
        if targetNum % idx == 0:
            return False
    return True


for i in data:
    if searchDecimal(i):
        result.append(i)

print(len(result))
