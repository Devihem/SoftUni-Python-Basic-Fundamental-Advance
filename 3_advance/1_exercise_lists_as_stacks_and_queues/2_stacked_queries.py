numbers_stack = []
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

    elif command.startswith(COMMAND_DELETE):
        numbers_stack.pop()

    elif command.startswith(COMMAND_MAXIMUM):
        print(max(numbers_stack))

    elif command.startswith(COMMAND_MINIMUM):
        print(min(numbers_stack))

print(*numbers_stack, sep=", ")
