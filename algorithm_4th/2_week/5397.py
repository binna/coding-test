import sys

n = int(input())
data = [sys.stdin.readline().rstrip() for _ in range(n)]

for info in data:
    queueLeft = []
    queueRight = []
    for target in info:
        if target == '<':
            if len(queueLeft) > 0:
                queueRight.append(queueLeft.pop(-1))
        elif target == '>':
            if len(queueRight) > 0:
                queueLeft.append(queueRight.pop(-1))
        elif target == '-':
            if len(queueLeft) > 0:
                queueLeft.pop(-1)
        else:
            queueLeft.append(target)
    print("".join(queueLeft) + "".join(reversed(queueRight)))
