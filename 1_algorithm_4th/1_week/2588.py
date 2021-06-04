inputValue = [int(input()) for _ in range(2)]

for i in str(inputValue[1])[::-1]:
    print(inputValue[0] * int(i))
print(inputValue[0] * inputValue[1])
