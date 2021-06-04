import sys

data = sys.stdin.readline().rstrip()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = []

for i in data:
    for j in dial:
        if j.find(i) != -1:
            result.append(dial.index(j) + 2)
print(sum(result) + len(result))
