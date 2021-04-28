import sys

data = []
checkZero = [0, 0]
while True:
    inputValue = list(map(int, sys.stdin.readline().rstrip().split()))
    if inputValue == checkZero:
        break
    data.append(inputValue)

for i in data:
    print(sum(i))
