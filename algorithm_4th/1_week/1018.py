import sys


def checkFixed(board):
    result = [0, 0]
    for i in range(0, len(board), 2):
        for j in range(0, len(board[i]), 2):
            if board[i][j] == 'B' and board[i][j + 1] == 'W' and board[i + 1][j] == 'W' and board[i + 1][j + 1] == 'B':
                continue
            if board[i][j] != 'B':
                result[0] += 1
            if board[i][j + 1] != 'W':
                result[0] += 1
            if board[i + 1][j] != 'W':
                result[0] += 1
            if board[i + 1][j + 1] != 'B':
                result[0] += 1
    for i in range(0, len(board), 2):
        for j in range(0, len(board[i]), 2):
            if board[i][j] == 'W' and board[i][j + 1] == 'B' and board[i + 1][j] == 'B' and board[i + 1][j + 1] == 'W':
                continue
            if board[i][j] != 'W':
                result[1] += 1
            if board[i][j + 1] != 'B':
                result[1] += 1
            if board[i + 1][j] != 'B':
                result[1] += 1
            if board[i + 1][j + 1] != 'W':
                result[1] += 1
    return min(result)


m, n = map(int, input().split())
data = [list(sys.stdin.readline().rstrip()) for _ in range(m)]
count = []
for idxM in range(m - 7):
    for idxN in range(n - 7):
        count.append(checkFixed([targetBoard[(0 + idxN):(8 + idxN)] for targetBoard in data[(0 + idxM):(8 + idxM)]]))
print(min(count))
