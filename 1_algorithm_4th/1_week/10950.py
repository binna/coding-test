inputNum = int(input())
data = [list(map(int, input().split())) for _ in range(inputNum)]

for i in data:
    print(sum(i))
