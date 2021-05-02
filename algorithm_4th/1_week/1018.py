import sys


def changePainting(color):
    if color == 'W':
        return 'B'
    if color == 'B':
        return 'W'


def checkFixed(board):
    result = 0
    for i in range(len(board)):
        if i < len(board) - 1:
            if board[i][0] == board[i + 1][0]:
                board[i + 1][0] = changePainting(board[i + 1][0])
                result += 1
        for j in range(len(board[i]) - 1):
            if board[i][j] == board[i][j + 1]:
                board[i][j + 1] = changePainting(board[i][j + 1])
                result += 1
    return result


m, n = map(int, input().split())
data = [list(sys.stdin.readline().rstrip()) for _ in range(m)]
count = []
for idxM in range(m - 7):
    for idxN in range(n - 7):
        count.append(checkFixed([targetBoard[(0+idxN):(8+idxN)] for targetBoard in data[(0+idxM):(8+idxM)]]))
print(min(count))
