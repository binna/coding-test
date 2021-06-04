import sys

alphabet = sys.stdin.readline().rstrip()
result = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

for i in range(len(alphabet)):
    if result[(ord(alphabet[i]) - 97)] == -1:
        result[(ord(alphabet[i]) - 97)] = i

for i in result:
    print(i, end=' ')
