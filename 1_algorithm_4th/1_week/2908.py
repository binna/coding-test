import sys

data = sys.stdin.readline().rstrip().split()
idx = 0

for i in data:
    tmp = ''
    for j in i[::-1]:
        tmp += j
    data[idx] = tmp
    idx += 1

if data[0] < data[1]:
    print(data[1])
else:
    print(data[0])
