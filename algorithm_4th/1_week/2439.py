inputN = int(input())

for i in range(1, inputN + 1):
    for j in range(0, inputN):
        if j < inputN - i:
            print(' ', end='')
        else:
            print('*', end='')
    print()
