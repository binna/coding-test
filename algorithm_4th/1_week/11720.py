import sys

n = int(input())
data = sys.stdin.readline().rstrip()

sumData = 0
for i in data:
    sumData += int(i)
print(sumData)
