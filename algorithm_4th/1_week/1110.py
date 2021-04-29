inputValue = input()

if int(inputValue) < 10:
    inputValue = '0' + inputValue

a, b = int(inputValue[1]), int(inputValue[1]) + int(inputValue[0])
cnt = 0
while True:
    cnt += 1
    tmp = str(a) + str(b)
    if inputValue == tmp:
        break
    a, b = b, (a + b) % 10
print(cnt)
