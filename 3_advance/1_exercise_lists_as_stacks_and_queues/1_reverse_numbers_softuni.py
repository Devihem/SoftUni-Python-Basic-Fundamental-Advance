from collections import deque

stack_1 = deque(input().split())
stack_1.reverse()

print(*stack_1)
