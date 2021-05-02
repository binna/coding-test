def checkSelfNumber(targetNumber):
    selfNum = targetNumber
    for idx in str(targetNumber):
        selfNum += int(idx)
    return selfNum


selfNumber = [True for _ in range(10000)]
for i in range(1, 10000 + 1):
    tmp = checkSelfNumber(i)
    if tmp < 10000 + 1:
        selfNumber[tmp - 1] = False

for i in range(len(selfNumber)):
    if selfNumber[i]:
        print(i + 1)
