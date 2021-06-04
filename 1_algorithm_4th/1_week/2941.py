import sys

data = sys.stdin.readline().rstrip()
croatiaAlphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatiaAlphabet:
    data = data.replace(i, '@')

print(len(data))
