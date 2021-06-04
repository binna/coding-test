from collections import deque

inputValue = int(input())
queue = deque()

for i in range(1, inputValue + 1):
    queue.append(i)
while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue.popleft())
