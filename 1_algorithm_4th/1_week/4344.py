import sys

n = int(input())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

for i in data:
    avgData = (sum(i) - i[0]) / i[0]
    cnt = 0
    for j in range(1, len(i)):
        if i[j] > avgData:
            cnt += 1
    print(str('%.3f' % round(cnt / i[0] * 100, 3) + '%'))
