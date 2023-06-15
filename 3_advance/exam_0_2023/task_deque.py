from collections import deque

list_deque_1 = deque([int(x) for x in input().split()])
list_deque_2 = deque([int(x) for x in input().split()])

while True:

    current_example1 = list_deque_1.pop()
    current_example2 = list_deque_2.popleft()