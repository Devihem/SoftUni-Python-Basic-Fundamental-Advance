from collections import deque

numbers_stack = deque()

map_function = {
    1: lambda x: numbers_stack.append(x[1]),
    2: lambda x: numbers_stack.pop() if numbers_stack else None,
    3: lambda x: print(max(numbers_stack)) if numbers_stack else None,
    4: lambda x: print(min(numbers_stack)) if numbers_stack else None,
}


for _ in range(int(input())):
    number_data = [int(x) for x in input().split()]
    map_function[number_data[0]](number_data)

numbers_stack.reverse()
print(*numbers_stack, sep=", ")
print(type(map_function))
