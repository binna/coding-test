a, b, c = int(input()), int(input()), int(input())

answer = a * b * c
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in str(answer):
    i = int(i)
    result[i] += 1

for i in result:
    print(i)
