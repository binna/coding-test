a, b = int(input()), int(input())
result = []


def searchDecimal(targetNum):
    if targetNum == 0 or targetNum == 1:
        return False
    for idx in range(2, targetNum):
        if targetNum % idx == 0:
            return False
    return True


for i in range(a, b + 1):
    if searchDecimal(i):
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))
