n = int(input())
board = [list(input()) for _ in range(n)]
result = 1


def checkRowAndCol(answer):
    for cnt_i in range(n):
        cnt = 1
        for cnt_j in range(1, n):
            if board[cnt_i][cnt_j - 1] == board[cnt_i][cnt_j]:
                cnt += 1
                answer = max(answer, cnt)
            else:
                cnt = 1

    for cnt_j in range(n):
        cnt = 1
        for cnt_i in range(1, n):
            if board[cnt_i - 1][cnt_j] == board[cnt_i][cnt_j]:
                cnt += 1
                answer = max(answer, cnt)
            else:
                cnt = 1
    return answer


for i in range(n):
    for j in range(n):
        if j + 1 < n:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            result = checkRowAndCol(result)
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

        if i + 1 < n:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            result = checkRowAndCol(result)
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(result)
