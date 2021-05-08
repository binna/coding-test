import sys
data = []

while True:
    tmp = sys.stdin.readline().rstrip()
    if tmp == '0 0 0':
        break
    data.append(list(map(int, tmp.split())))

for i in data:
    i.sort()
    if i[0] ** 2 + i[1] ** 2 == i[2] ** 2:
        print("right")
    else:
        print("wrong")
