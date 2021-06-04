# 시간 : 10320ms
# import sys
# n = int(sys.stdin.readline().rstrip())
# data = [0] * 10000
#
# for _ in range(n):
#     data[int(sys.stdin.readline().rstrip()) - 1] += 1
# for i in range(10000):
#     if data[i] != 0:
#         for _ in range(data[i]):
#             print(i + 1)


# 시간 : 9712ms
import sys
n = int(sys.stdin.readline())
data = [0] * 10000

for _ in range(n):
    data[int(sys.stdin.readline()) - 1] += 1
for i in range(10000):
    if data[i] != 0:
        for _ in range(data[i]):
            print(i + 1)
