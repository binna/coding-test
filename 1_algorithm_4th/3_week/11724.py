import sys
sys.setrecursionlimit(10 ** 8)

n, m = map(int, input().split())
gr = [[False] * (n + 1) for _ in range(n + 1)]  # 인접행렬, 1부터 시작하기 때문에 + 1 해줌

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    gr[a][b] = True
    gr[b][a] = True


def dfs(target):
    chk[target] = True
    for nextTarget in range(1, n + 1):
        if gr[target][nextTarget] and not chk[nextTarget]:
            dfs(nextTarget)


cnt = 0
chk = [False] * (n + 1)
for i in range(1, n + 1):
    if not chk[i]:
        cnt += 1
        dfs(i)

print(cnt)
