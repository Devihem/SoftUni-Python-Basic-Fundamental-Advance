from collections import deque

numbers_stack = deque()
number_of_commands = int(input())

COMMAND_PUSH = '1'
COMMAND_DELETE = '2'
COMMAND_MAXIMUM = '3'
COMMAND_MINIMUM = '4'

for command_number in range(number_of_commands):

    command = input()

    if command.startswith(COMMAND_PUSH):
        number = command.split()
        numbers_stack.append(int(number[1]))

    if len(numbers_stack) > 0:
        if command.startswith(COMMAND_DELETE):
            numbers_stack.pop()

        elif command.startswith(COMMAND_MAXIMUM):
            print(max(numbers_stack))

        elif command.startswith(COMMAND_MINIMUM):
            print(min(numbers_stack))

numbers_stack.reverse()
print(*numbers_stack, sep=", ")
