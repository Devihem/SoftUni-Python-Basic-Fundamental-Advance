matrix_size = 6
matrix = [input().split() for x in range(matrix_size)]

loc_r, loc_c = input().strip('(').strip(')').split(', ')

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

    command, direction, *values = input().split(', ')

    if command == "Create":
        pass
    elif command == "Update":
        pass
    elif command == "Delete":
        pass
    elif command == "Read":
        pass

# Finding UNIT place:
row_r, row_c = [(row, col)
                for col in range(matrix_size)
                for row in range(matrix_size) if map_matrix[row][col] == 'SYMBOL'][0]
