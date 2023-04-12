parentheses_input = input()
stack = []
for symbol in parentheses_input:
    if symbol in ['[', '{', '(']:
        stack.append(symbol)
    else:
        if not stack:
            print("NO")
            break
        if symbol == ']' and stack[-1] != '[':
            print("NO")
            break
        elif symbol == '}' and stack[-1] != '{':
            print("NO")
            break
        elif symbol == ')' and stack[-1] != '(':
            print("NO")
            break
        else:
            stack.pop()
else:
    print("YES")
