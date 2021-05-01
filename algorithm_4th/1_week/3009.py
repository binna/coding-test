import sys
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(3)]
colX = []
colY = []


def printPoint(point):
    for idx in point:
        if point.count(idx) % 2 != 0:
            print(idx, end=' ')


for i in data:
    colX.append(i[0])
    colY.append(i[1])
printPoint(colX)
printPoint(colY)
