n = int(input())
data = [int(input()) for _ in range(n)]
decimalList = [True for _ in range(10000)]

decimalList[0] = False
for i in range(2, int(10000 ** 0.5)):
    if decimalList[i - 1]:
        for j in range(i + i, 10000, i):
            decimalList[j - 1] = False

for i in data:
    idx = 0
    while True:
        if decimalList[(i - 1) // 2 - idx] and decimalList[(i - 1) // 2 + idx]:
            print((i - 1) // 2 - idx + 1, (i - 1) // 2 + idx + 1)
            break
        idx += 1
