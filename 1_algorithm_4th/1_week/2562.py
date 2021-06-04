import sys

data = []
for i in range(9):
    data.append(int(sys.stdin.readline().rstrip()))

maxData = max(data)
print('{}\n{}'.format(maxData, data.index(maxData) + 1))
