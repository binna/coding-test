inputValue = int(input())
result = 0

if inputValue == 1:
    print(1)
else:
    idx = 1
    bee = 1
    while True:
        bee += (idx * 6)
        idx += 1
        if inputValue <= bee:
            print(idx)
            break
