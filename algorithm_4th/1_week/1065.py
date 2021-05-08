inputValue = int(input())
cnt = 0

for i in range(1, inputValue + 1):
    if i < 100:
        cnt += 1
    else:
        tmp = str(i)
        flag = True
        for j in range(len(tmp) - 2):
            difference1 = int(tmp[j + 1]) - int(tmp[j])
            difference2 = int(tmp[j + 2]) - int(tmp[j + 1])
            if difference1 != difference2:
                flag = False
                break
        if flag:
            cnt += 1
print(cnt)
