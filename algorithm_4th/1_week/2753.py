inputValue = int(input())

if (inputValue % 4 == 0 and inputValue % 100 != 0) or inputValue % 400 == 0:
    print(1)
else:
    print(0)
