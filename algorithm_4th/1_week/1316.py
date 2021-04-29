import sys
n = int(input())
data = [sys.stdin.readline().rstrip() for _ in range(n)]
cnt = 0

for i in data:
    flag = True
    word = []
    beforeWord = ''
    for j in range(1, len(i)):
        if j == 1:
            if i[0] == i[1]:
                beforeWord = i[0]
            else:
                beforeWord = i[1]
                word.append(i[1])
            word.append(i[0])
        else:
            if i[j] in word:
                if beforeWord == i[j]:
                    continue
                flag = False
                break
            beforeWord = i[j]
            word.append(i[j])
    if flag:
        cnt += 1
print(cnt)
