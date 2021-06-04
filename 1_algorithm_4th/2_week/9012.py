for _ in range(int(input())):
    data = input()
    stack = []
    answer = 'YES'
    for targetCh in data:
        if targetCh == '(':
            stack.append(targetCh)
        else:
            if len(stack) == 0:
                answer = 'NO'
                break
            else:
                stack.pop(-1)
    if len(stack) > 0:
        answer = 'NO'
    print(answer)
