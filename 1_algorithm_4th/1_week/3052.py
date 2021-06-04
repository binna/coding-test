# 시간 : 116ms
# import sys
#
# data = [int(sys.stdin.readline().rstrip()) for _ in range(10)]
# result = {}
#
# for i in data:
#     if i % 42 in result.keys():
#         result[i % 42] += 1
#     else:
#         result[i % 42] = 1
#
# print(len(result))


# 시간 : 104ms
# import sys
#
# data = [int(sys.stdin.readline().rstrip()) for _ in range(10)]
# result = []
#
# for i in data:
#     if i % 42 not in result:
#         result.append(i % 42)
#
# print(len(result))


# 시간 : 112ms
# import sys
#
# data = [int(sys.stdin.readline().rstrip()) for _ in range(10)]
# result = set()
#
# for i in data:
#     result.add((lambda targetNum: targetNum % 42)(i))
#
# print(len(result))


# 시간 108ms
import sys

data = [int(sys.stdin.readline().rstrip()) for _ in range(10)]
result = set()

for i in data:
    if i % 42 not in result:
        result.add(i % 42)

print(len(result))
