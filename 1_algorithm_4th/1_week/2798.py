import sys
from itertools import combinations

n, sumMixNum = map(int, input().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

result = sumMixNum
resultSum = 0
for i in combinations(data, 3):
    difference = sumMixNum - sum(i)
    if 0 <= difference < result:
        result = sumMixNum - sum(i)
        resultSum = sum(i)
print(resultSum)
