import sys

inputN = int(input())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(inputN)]

cnt = 1
for i in data:
    print('Case #{}: {} + {} = {}'.format(cnt, i[0], i[1], sum(i)))
    cnt = cnt + 1
