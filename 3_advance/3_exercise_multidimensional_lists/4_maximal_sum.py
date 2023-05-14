number_of_rows, number_of_columns = map(int, input().split(' '))

matrix = [[row for row in input().split(' ')] for _ in range(number_of_rows)]
max_3_3_sub_matrix_sum = float('-inf')
max_3_3_sub_matrix = []

for row in range(number_of_rows - 2):
    for column in range(number_of_columns - 2):
        current_sum = 0
        current_matrix = []
        for sub_row in range(row, row + 3):
            sub_current_matrix = []
            for sub_column in range(column, column + 3):
                sub_current_matrix.append(int(matrix[sub_row][sub_column]))
                current_sum += int(matrix[sub_row][sub_column])
            current_matrix += [sub_current_matrix]

        if current_sum > max_3_3_sub_matrix_sum:
            max_3_3_sub_matrix_sum = current_sum
            max_3_3_sub_matrix = current_matrix

print(f'Sum = {max_3_3_sub_matrix_sum}')
[print(*row) for row in max_3_3_sub_matrix]

