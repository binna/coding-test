data = input()
stack = []
result = ''

for target in data:
    if target.isalpha():
        result += target
    else:
        if target == '(':
            stack.append(target)
        elif target == '*' or target == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(target)
        elif target == '+' or target == '-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(target)
        elif target == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

while stack:
    result += stack.pop()
print(result)
