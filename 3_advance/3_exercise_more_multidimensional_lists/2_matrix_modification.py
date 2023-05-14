matrix_size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(matrix_size)]
data_range = range(matrix_size)

while True:

    command, *data = input().split()

    # While loop - breakpoint and final print
    if command == 'END':
        [print(*row) for row in matrix]
        break

    # Check, for number of elements and there range
    if len(data) != 3 or int(data[0]) not in data_range or int(data[1]) not in data_range:
        print("Invalid coordinates")
        continue

    # Command coordinates r, c
    r, c, value = [int(number) for number in data]

    # Commands Add and Subtract
    if command == 'Add':
        matrix[r][c] += value
    elif command == 'Subtract':
        matrix[r][c] -= value
