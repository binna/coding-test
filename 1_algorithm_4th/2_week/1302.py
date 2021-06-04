n = int(input())
data = [input() for _ in range(n)]
result = {}

for target in data:
    if target in result.keys():
        result[target] += 1
    else:
        result[target] = 1

maxNum = max(result.values())
answer = []
for k, v in result.items():
    if v == maxNum and not(k in answer):
        answer.append(k)
print(sorted(answer)[0])
