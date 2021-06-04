import sys

n, x = map(int, input().split())
# a = [map(int, sys.stdin.readline().rstrip().split())]
a = list(map(int,  sys.stdin.readline().rstrip().split()))

for i in a:
    if i < x:
        print(i, end=' ')
