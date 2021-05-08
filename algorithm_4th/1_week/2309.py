from itertools import combinations

inputValue = [int(input()) for _ in range(9)]

for i in combinations(inputValue, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break
