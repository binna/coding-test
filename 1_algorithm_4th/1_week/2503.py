import sys
from itertools import permutations

n = int(input())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
testCase = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

cnt = 0
for test in testCase:
    flag = True
    for i in range(n):
        strike = 0
        ball = 0
        tmp = list(str(data[i][0]))
        for j in range(3):
            if tmp[j] == str(test[j]):
                tmp[j] = '@'
                strike += 1
            elif tmp[j] in str(test):
                tmp[j] = '#'
                ball += 1
        if strike != data[i][1] or ball != data[i][2]:
            flag = False
            break
    if flag:
        cnt += 1
print(cnt)
