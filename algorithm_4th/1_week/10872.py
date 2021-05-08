n = int(input())
result = 1
for i in range(1, n + 1):
    result *= i
if n == 0:
    print(1)
else:
    print(result)
