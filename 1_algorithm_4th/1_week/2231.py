n = int(input())
result = 0

for i in range(n):
    sumData = i
    for j in str(i):
        sumData += int(j)
    if sumData == n:
        result = i
        break
print(result)
