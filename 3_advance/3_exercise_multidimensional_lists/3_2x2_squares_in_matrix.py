number_of_rows, number_of_columns = map(int, input().split(' '))

matrix = [[row for row in input().split(' ')] for _ in range(number_of_rows)]
total_same_blocks = 0

for row in range(number_of_rows - 1):
    for column in range(number_of_columns - 1):
        current_symbol = matrix[row][column]
        current_counter = 0
        for sub_row in range(row, row + 2):
            for sub_column in range(column, column + 2):
                if matrix[sub_row][sub_column] != current_symbol:
                    break
                else:
                    current_counter += 1

        if current_counter == 4:
            total_same_blocks += 1

print(total_same_blocks)