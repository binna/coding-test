import sys
data = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = -1

if data[1] < data[2]:
    cnt = int(data[0] / (data[2] - data[1]) + 1)
print(cnt)
