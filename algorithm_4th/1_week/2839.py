inputValue = int(input())
cnt = 0

if inputValue % 3 != 0:
    cnt = int(inputValue / 5)
    inputValue %= 5
print(inputValue)
if inputValue % 3 == 0:
    inputValue / 3
else:
    cnt = -1


print(cnt)
