primeNumList = [True for _ in range(123456 * 2)]

primeNumList[0] = False
for i in range(2, int((123456 * 2) ** 0.5)):
    if primeNumList[i - 1]:
        for j in range(i + i, 123456 * 2, i):
            primeNumList[j - 1] = False

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    if n == 1:
        cnt = 1
    for i in range(n + 1, 2 * n):
        if primeNumList[i - 1]:
            cnt += 1
    print(cnt)
