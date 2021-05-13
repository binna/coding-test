import sys

r, c = map(int, input().split())
board = [sys.stdin.readline() for _ in range(r)]
chk = [False] * 26      # 알파벳 방문 체크
answer = 0

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


def is_valid(targetY, targetX):
    return 0 <= targetY < r and 0 <= targetX < c


def backtrackingDfs(y, x, d):   # 백트래킹 + DFS
    global answer
    answer = max(answer, d)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        nd = d + 1
        if is_valid(ny, nx) and not chk[ord(board[ny][nx]) - ord('A')]:
            chk[ord(board[ny][nx]) - ord('A')] = True
            backtrackingDfs(ny, nx, nd)
            chk[ord(board[ny][nx]) - ord('A')] = False


chk[ord(board[0][0]) - ord('A')] = True
backtrackingDfs(0, 0, 1)
print(answer)
