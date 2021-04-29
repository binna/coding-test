result = []
for i in range(100):
    result.append(True)

for i in range(1, 100 + 1):
    if i + i < 100:
        result[i + i - 1] = False

for i in range(len(result)):
    if result[i]:
        print(i + 1)
