import sys
m, n = map(int, input().split())
data = [list(sys.stdin.readline().rstrip()) for _ in range(m)]
result = 0


def changePainting(color):
    if color == 'W':
        return 'B'
    if color == 'B':
        return 'W'


for i in range(len(data)):
    if i < len(data) - 1:
        if data[i][0] == data[i + 1][0]:
            data[i + 1][0] = changePainting(data[i + 1][0])
            result += 1
    for j in range(len(data[i]) - 1):
        if data[i][j] == data[i][j + 1]:
            data[i][j + 1] = changePainting(data[i][j + 1])
            result += 1
print(result)
for i in data:
    print(i)
