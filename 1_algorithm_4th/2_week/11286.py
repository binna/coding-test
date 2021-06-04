import heapq
import sys

n = int(sys.stdin.readline().rstrip())
arr = []

for _ in range(n):
    inputValue = int(sys.stdin.readline())
    if inputValue == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr)[1])
    else:
        heapq.heappush(arr, (abs(inputValue), inputValue))
