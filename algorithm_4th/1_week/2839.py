inputValue = int(input())
flag = True
result = -1

if inputValue / 5 > 0:
    for i in range(int(inputValue / 5), 0, -1):
        if inputValue - (i * 5) == 0:
            result = i
            flag = False
            break
        elif (inputValue - (i * 5)) % 3 == 0:
            result = int((inputValue - (i * 5)) / 3 + i)
            flag = False
            break
    if flag:
        if inputValue % 3 == 0:
            result = int(inputValue / 3)
print(result)
