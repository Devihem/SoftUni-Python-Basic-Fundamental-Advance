matrix_size = 0



# Type 1 - 4 axis:
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# Type 2 8-axis:


# Finding UNIT place:
row_r, row_c = [(row, col)
                for col in range(matrix_size)
                for row in range(matrix_size) if map_matrix[row][col] == 'SYMBOL'][0]
