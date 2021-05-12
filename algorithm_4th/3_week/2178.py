from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

n, m = map(int, input().split())
board = [input() for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dq = deque()
dq.append((0, 0, 1))
chk[0][0] = True


def is_valid(targetY, targetX):
    return 0 <= targetY < n and 0 <= targetX < m


while len(dq) > 0:
    y, x, d = dq.popleft()

    if y == n - 1 and x == m - 1:
        print(d)
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        nd = d + 1
        if is_valid(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
            chk[ny][nx] = True
            dq.append((ny, nx, nd))
