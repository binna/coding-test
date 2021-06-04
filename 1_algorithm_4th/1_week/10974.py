from itertools import permutations
n = int(input())
data = [i + 1 for i in range(n)]

for i in permutations(data, n):
    for j in i:
        print(j, end=' ')
    print()
