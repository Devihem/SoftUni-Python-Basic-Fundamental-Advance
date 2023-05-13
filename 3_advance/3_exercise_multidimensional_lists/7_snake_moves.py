matrix_row, matrix_column = map(int, input().split(' '))
matrix = [[' ' for _ in range(matrix_column)] for _ in range(matrix_row)]

snake_word = list(input())
current_symbol = ''

for row in range(matrix_row):
    if row % 2 == 0:
        range_column_start = 0
        range_column_end = matrix_column
        step = 1
    else:
        range_column_start = matrix_column - 1
        range_column_end = -1
        step = -1
    for column in range(range_column_start, range_column_end, step):
        current_symbol = snake_word.pop(0)
        snake_word.append(current_symbol)
        matrix[row][column] = current_symbol

[print(''.join(row)) for row in matrix]
