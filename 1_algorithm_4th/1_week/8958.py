import sys

n = int(input())
data = [sys.stdin.readline().rstrip() for _ in range(n)]

accumulation = 0
result = 0
for i in data:
    for j in i:
        if j == 'O':
            accumulation += 1
            result += accumulation
        else:
            accumulation = 0
    print(result)
    accumulation = 0
    result = 0
