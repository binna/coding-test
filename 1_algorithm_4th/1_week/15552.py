# 시간 : 1904ms
# inputNum = int(input())
# data = [list(map(int, input().split())) for _ in range(inputNum)]
#
# for i in data:
#     print(sum(i))


# 시간 : 1068ms
# import sys
#
# inputNum = int(input())
# data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(inputNum)]
#
# for i in data:
#     print(sum(i))


# 시간 : 1112ms
import sys

inputNum = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(inputNum)]

for i in data:
    print(sum(i))
