stack_1 = input().split()
stack_2 = []
while len(stack_1) > 0:
    stack_2.append(stack_1.pop())
print(*stack_2)
