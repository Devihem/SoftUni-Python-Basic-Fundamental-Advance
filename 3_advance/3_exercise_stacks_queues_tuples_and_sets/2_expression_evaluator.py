from collections import deque
from math import floor

symbols_queue = deque(input().split())

working_numbers = deque([])

while len(symbols_queue) > 0:
    current_symbol = symbols_queue.popleft()
    if current_symbol.lstrip("-").isdigit():
        working_numbers.append(int(current_symbol))
        continue

    while len(working_numbers) > 1:
        a = working_numbers.popleft()
        b = working_numbers.popleft()
        c = 0
        if current_symbol == "+":
            c = a + b
        elif current_symbol == "-":
            c = a - b
        elif current_symbol == "*":
            c = a * b
        elif current_symbol == "/":
            c = floor(a / b)

        working_numbers.appendleft(c)
    new_number = str(working_numbers.popleft())
    symbols_queue.appendleft(new_number)

print(*working_numbers)
