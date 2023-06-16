matrix_size = 6
matrix = [input().split() for x in range(matrix_size)]

loc_r, loc_c = [int(x) for x in input().strip('(').strip(')').split(', ')]


# Type 1 - 4 axis:
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:

    command_data = input()
    if command_data == 'Stop':
        break

    command, direction, *values = command_data.split(', ')
    update_r, update_c = directions[direction]

    loc_r += update_r
    loc_c += update_c

    if command == "Create":
        if matrix[loc_r][loc_c] == '.':
            matrix[loc_r][loc_c] = values[0]

    elif command == "Update":
        if matrix[loc_r][loc_c] != '.':
            matrix[loc_r][loc_c] = values[0]

    elif command == "Delete":
        matrix[loc_r][loc_c] = '.'

    elif command == "Read":
        if matrix[loc_r][loc_c] != '.':
            print(matrix[loc_r][loc_c])

[print(' '.join(x))for x in matrix]
# # Finding UNIT place:
# row_r, row_c = [(row, col)
#                 for col in range(matrix_size)
#                 for row in range(matrix_size) if map_matrix[row][col] == 'SYMBOL'][0]
