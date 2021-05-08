import sys
n = int(input())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

for i in range(len(data)):
    rank = 1
    for j in range(len(data)):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            rank += 1
    print(rank, end=' ')
