import sys
x, y, w, h = map(int, sys.stdin.readline().rstrip().split())
distance = [abs(0 - x), abs(x - w), abs(0 - y), abs(y - h)]
print(min(distance))
