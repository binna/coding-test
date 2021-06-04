import sys

n = int(input())
data = list(map(int, sys.stdin.readline().rstrip().split()))
maxData = max(data)

for i in range(len(data)):
    data[i] = data[i] / maxData * 100

print(sum(data) / n)
