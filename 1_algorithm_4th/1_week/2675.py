import sys

n = int(input())
data = [sys.stdin.readline().rstrip() for _ in range(n)]

for i in data:
    for j in range(2, len(i)):
        print(i[j] * int(i[0]), end='')
    print()
