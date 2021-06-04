import sys

alphabet = sys.stdin.readline().rstrip()
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in alphabet:
    targetAlphabet = ord(i)
    if targetAlphabet >= 97:
        result[targetAlphabet - 97] += 1
        continue
    result[targetAlphabet - 65] += 1

cnt = 0
maxData = max(result)
for i in result:
    if i == maxData:
        cnt += 1
if cnt != 1:
    print('?')
else:
    print(chr(result.index(maxData) + 65))
